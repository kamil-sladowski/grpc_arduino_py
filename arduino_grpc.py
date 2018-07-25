from __future__ import print_function

import grpc

import canal_data_pb2
import canal_data_pb2_grpc
import serial
from time import sleep


PORT = '/dev/ttyS2'


class ArduinoListener:

    def __init__(self, port, baudrate):
        self.port_listener = serial.Serial(port=port,
                                           baudrate=baudrate,
                                           parity=serial.PARITY_NONE,
                                           stopbits=serial.STOPBITS_ONE,
                                           bytesize=serial.EIGHTBITS,
                                           timeout=5)
        print("Listening port: STARTED")

    def led_on(self):
        self.port_listener.write(b'1')

    def led_off(self):
        self.port_listener.write(b'0')

    def control_led(self):
        i = 0
        while i < 10:
            print(i)
            self.led_on()
            sleep(1)
            self.ledOff()
            sleep(1)
            i += 1
        print("end")


class GRPC_Transmitter:

    def __init__(self, hostname, port):
        self.channel = grpc.insecure_channel(hostname + ':' + port)
        self.stub = canal_data_pb2_grpc.SendingSoundDataStub(self.channel)

    def send_sound_via_protobuffers(self, frequency, timestamp):

        response = self.stub.sendSoundData(canal_data_pb2.SoundMessage(
            frequency=frequency,
            timestamp=timestamp
        ))
        sleep(2)


if __name__ == '__main__':
    timestamp = 11010101212
    frequency = 3334

    arduino = ArduinoListener(PORT, 9600)
    grpc = GRPC_Transmitter('localhost', '50051')

    arduino.controlLed()
    # grpc.send_sound_via_protobuffers(frequency, timestamp)
