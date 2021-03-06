import socket
from threading import Thread
from socketserver import ThreadingMixIn
from SocketScripts import SocketManage
from SocketScripts import SocketHelper as helper


# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread):

    def __init__(self, ip, port):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.smanage = SocketManage.SocketManage()
        print ("[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        while True:
            try:
                data = conn.recv(1024)
                print("__has data")
                if data:
                    print(data)
                    data = helper.convertToString(data)
                    #print ("Server received data:", data)
                    self.smanage.testdata(data,conn)
                else:
                    print("__Else")
                    conn.close()
            except Exception:
                conn.close()
                return False
            # MESSAGE = input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            # if MESSAGE == 'exit':
            #     break
            # conn.send(helper.convertToBytes(MESSAGE))  # echo

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0'
TCP_PORT = 2004
BUFFER_SIZE = 20  # Usually 1024, but we need quick response

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpServer.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpServer.listen(1)
    print ("Multithreaded Python server : Waiting for connections from TCP clients...")
    try:
        (conn, (ip, port)) = tcpServer.accept()
    except Exception:
        continue
    newthread = ClientThread(ip, port)
    newthread.start()
    threads.append(newthread)
    for t in threads:
        t.join()