from SocketScripts import SocketConnect2
if __name__ == '__main__':
    try:
        socket = SocketConnect2.ThreadedServer(serverHost='192.168.1.200')
        socket.startServer()
    except KeyboardInterrupt:
        exit(0)