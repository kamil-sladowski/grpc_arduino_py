FROM python
RUN pip install --upgrade pip
RUN pip install pyserial grpcio-tools googleapis-common-protos
   && mkdir /home/microphone
   && git clone https://github.com/kamilo116/grpc_arduino_py.git /home/microphone
   && cd /home/microphone
   && python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. canal_data.proto
CMD python /home/microphone/arduino_grpc.py
