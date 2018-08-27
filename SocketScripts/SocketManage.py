from socket import *
import time
from threading import Thread

class SocketManage(Thread):

    def __init__(self, data):
        Thread.__init__(self)
        self.data = data #string
        print("[+/] New thread started for client data")

    def run(self):
        while True:
            if (self.data == "help"):
                print("this is a test")
                break