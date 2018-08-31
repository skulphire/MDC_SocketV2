import os
from SocketScripts import globals
def clearDictsOfClient(client):
    print("Removing user")
    globals.AREUSERSLOGGEDIN[globals.CONNECTIONS[client]] = False
    del globals.CLIENTIPS[globals.CONNECTIONS[client]]
    del globals.CONNECTIONS[client]

def closingClient(client,disconnectMessage):
    if(client in globals.CONNECTIONS):
        try:
            print("Closing "+globals.CONNECTIONS[client]+"for: "+disconnectMessage)
            clearDictsOfClient(client)
        except Exception:
            print("Closing Client for: "+disconnectMessage)
    else:
        print("Closing Client for: "+disconnectMessage)
    client.close()

def initValidUsers(org = "ADPS"):
    userDir = org+"-Users/"
    workingDir = os.getcwd()
    dir = workingDir + "/MDC-Files/" + userDir
    try:
        globals.VALIDUSERS = os.listdir(dir)
        for user in globals.VALIDUSERS:
            print("User>"+user)
            globals.AREUSERSLOGGEDIN[user] = False
    except Exception:
        print("No Files Found in: "+dir)

def convertToString(bite):
    str = bite.decode("utf-8")
    return str
def convertToBytes(str):
    byteStr = bytes(str, 'utf-8')
    return byteStr