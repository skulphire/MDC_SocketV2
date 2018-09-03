# Python TCP Client B
import socket
from SocketScripts import SocketHelper as helper
import os
import time

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
            file = os.path.realpath(os.getcwd()+"/TempObjects/")+"/senarioData_21146.json"
            print(file)
            with open(file) as f:
                lines = f.readlines()
            tcpClientB.send(helper.convertToBytes("#senario"))
            print("#senario")
            d = tcpClientB.recv(BUFFER_SIZE)
            print(helper.convertToString(d))
            for line in lines:
                tcpClientB.send((helper.convertToBytes(line)))
                time.sleep(.1)
                #print(line)
            tcpClientB.send(helper.convertToBytes("#end-senario"))
            print("#end-senario")
    tcpClientB.close()
except:
    tcpClientB.close()
