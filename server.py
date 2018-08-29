from SocketScripts import SocketConnect2
if __name__ == '__main__':
    try:
        socket = SocketConnect2.ThreadedServer(serverPort=20000)
        socket.startServer()
    except KeyboardInterrupt:
        exit(0)