# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\x12\x07message\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"[\n\x07Message\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x14\n\x0cmessage_text\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"h\n\x14\x41ppendMessageRequest\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x14\n\x0cmessage_text\x18\x02 \x01(\t\x12.\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"<\n\x12\x41ppendMessageReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rresponse_text\x18\x02 \x01(\t\"^\n\x13GetAllMessagesReply\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x15\n\rresponse_text\x18\x02 \x01(\t\x12\x1f\n\x05items\x18\x03 \x03(\x0b\x32\x10.message.Message2\xad\x01\n\x12MessageReplication\x12M\n\rAppendMessage\x12\x1d.message.AppendMessageRequest\x1a\x1b.message.AppendMessageReply\"\x00\x12H\n\x0eGetAllMessages\x12\x16.google.protobuf.Empty\x1a\x1c.message.GetAllMessagesReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE._serialized_start=88
  _MESSAGE._serialized_end=179
  _APPENDMESSAGEREQUEST._serialized_start=181
  _APPENDMESSAGEREQUEST._serialized_end=285
  _APPENDMESSAGEREPLY._serialized_start=287
  _APPENDMESSAGEREPLY._serialized_end=347
  _GETALLMESSAGESREPLY._serialized_start=349
  _GETALLMESSAGESREPLY._serialized_end=443
  _MESSAGEREPLICATION._serialized_start=446
  _MESSAGEREPLICATION._serialized_end=619
# @@protoc_insertion_point(module_scope)