# Python TCP Client B
import socket
from SocketScripts import SocketHelper as helper

host = "opsidiumdesigns.com"
port = 9130
BUFFER_SIZE = 2000
MESSAGE = input("tcpClientB: Enter message/ Enter exit:")

tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpClientB.connect((host, port))
try:
    while MESSAGE != 'exit':
        tcpClientB.send(helper.convertToBytes(MESSAGE))
        data = tcpClientB.recv(BUFFER_SIZE)
        print(" Client received data:", data)
        MESSAGE = input("tcpClientB: Enter message to continue/ Enter exit:")
        tcpClientB.close()
except:
    tcpClientB.close()
