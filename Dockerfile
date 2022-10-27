FROM python:3.7

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app

RUN python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/message.proto

CMD ["python3", "main.py"]
