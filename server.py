from SocketScripts import SocketConnect
if __name__ == '__main__':
    try:
        SocketConnect.ClientThread
    except KeyboardInterrupt:
        exit(0)