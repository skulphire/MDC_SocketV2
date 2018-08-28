import socket
import threading
from SocketScripts import SocketManage
from SocketScripts import SocketHelper as helper

class ThreadedServer(object):
    def __init__(self,serverHost = '0.0.0.0', serverPort = 2004):
        self.ip = serverHost
        self.port = serverPort
        self.smanage = SocketManage.SocketManage()

    def startServer(self):
        print("Starting server...")
        self.tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpServer.bind((self.ip, self.port))
        self.tcpServer.listen(1)
        while True:
            client, (clientip,clientport) = self.tcpServer.accept()
            threading.Thread(target=self.clienthandler, args=(client,)).start()
            print("[+] New server socket thread started for " + clientip + ":" + str(clientport))

    def clienthandler(self,client):
        while True:
            try:
                data = client.recv(1024)
                if data:
                    data = helper.convertToString(data)
                    self.smanage.testdata(data,client)
            except Exception:
                break
        print("Closing client")
        print("[-] Server socket thread stopped for...")