# Python TCP Client B
import socket
from SocketScripts import SocketHelper as helper
import os

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
        if("json" in MESSAGE):
            file = os.path.realpath(os.getcwd()+"TempObjects/")+"senarioData_21146.json"
            with open(file) as f:
                lines = f.readlines()
            tcpClientB.send(helper.convertToBytes("#senario"))
            d = tcpClientB.recv(BUFFER_SIZE)
            print(helper.convertToString(d))
            for line in lines:
                tcpClientB.send((helper.convertToBytes(line)))
                print(line)
            tcpClientB.send(helper.convertToBytes("#end-senario"))
    tcpClientB.close()
except:
    tcpClientB.close()
