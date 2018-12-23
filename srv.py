import socket
import sys

# Define global constants
HOST = 'localhost'
PORT = 8888
BUFFER = 1024

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((HOST, PORT))

while 1:
    data, addr = soc.recvfrom(BUFFER)


    msg = data.decode('ascii')

    print(msg)


soc.close()