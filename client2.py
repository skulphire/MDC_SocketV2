# Python TCP Client B
import socket
from SocketScripts import SocketHelper as helper

host = "10.10.1.131"
port = 30120
BUFFER_SIZE = 2000
MESSAGE = input("tcpClientB: Enter message/ Enter exit:")

tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientB.connect((host, port))

while MESSAGE != 'exit':
    tcpClientB.send(helper.convertToBytes(MESSAGE))
    data = tcpClientB.recv(BUFFER_SIZE)
    print(" Client received data:", data)
    MESSAGE = input("tcpClientB: Enter message to continue/ Enter exit:")

tcpClientB.close()