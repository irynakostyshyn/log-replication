import asyncio
import json
from contextlib import suppress

import grpc
from aiohttp import web
from grpc.experimental.aio import init_grpc_aio

from message_pb2 import AppendMessageReply
from message_pb2_grpc import add_MessageReplicationServicer_to_server, MessageReplicationServicer

message_list = []


class MessageView(web.View):
    async def get(self) -> web.Response:
        return web.Response(body=json.dumps(message_list))


class Application(web.Application):
    def __init__(self):
        super().__init__()
        self.add_routes()

    def add_routes(self):
        self.router.add_view('/messages', MessageView)

    def run(self):
        return web.run_app(self, port=8000)


class MessageServicer(MessageReplicationServicer):
    def AppendMessage(self, request, context):
        messages = {"id": request.id, "message_text": request.message_text,
                    "created_at": {"seconds": request.created_at.seconds, "nanos": request.nanos}}
        print('got messages')

        message_list.append(messages)

        response = AppendMessageReply()
        response.success = True
        response.response_text = "Replicated successfully"
        return response


class GrpcServer:
    def __init__(self):
        init_grpc_aio()
        self.server = grpc.experimental.aio.server()
        self.servicer = MessageServicer()
        add_MessageReplicationServicer_to_server(
            self.servicer,
            self.server)
        self.server.add_insecure_port("[::]:50051")

    async def start(self):
        print("STARTING")
        await self.server.start()
        await self.server.wait_for_termination()

    async def stop(self):
        await self.server.close()
        await self.server.wait_for_termination()


async def run_grpc_server(app):
    try:
        server = GrpcServer()
        await server.start()
    except asyncio.CancelledError:
        pass
    finally:
        await server.stop()


async def subtask_wrapped(app):
    task = asyncio.create_task(run_grpc_server(app))

    yield

    task.cancel()
    with suppress(asyncio.CancelledError):
        await task  # Ensure any exceptions etc. are raised.


application = Application()

if __name__ == '__main__':
    application.cleanup_ctx.append(subtask_wrapped)
    application.run()
