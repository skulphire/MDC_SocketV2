import socket
import threading
from SocketScripts import SocketManage
from SocketScripts import SocketHelper as helper

class ThreadedServer(object):
    def __init__(self,serverHost = '10.10.1.131', serverPort = 30120):
        self.ip = serverHost
        self.port = serverPort
        self.smanage = SocketManage.SocketManage()

    def startServer(self):
        print("Starting server...")
        self.tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpServer.bind((self.ip, self.port))
        print("Server Binded to> "+self.ip+", "+str(self.port))
        self.tcpServer.listen(1)
        print("awating connections...")
        helper.initValidUsers()
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
                    print(data)
                    self.smanage.testdata(data,client)
            except Exception:
                break
        helper.closingClient(client,"Disconnect")
        print("[-] Server socket thread stopped for...")