import os
from SocketScripts import globals
def clearDictsOfClient(client):
    print("Removing user")
    globals.AREUSERSLOGGEDIN[globals.CONNECTIONS[client]] = False
    del globals.CLIENTIPS[globals.CONNECTIONS[client]]
    del globals.CONNECTIONS[client]

def closingClient(client,disconnectMessage):
    if(client in globals.CONNECTIONS):
        user = globals.CONNECTIONS[client]
        try:
            print("Closing "+globals.CONNECTIONS[client]+" for: "+disconnectMessage)
            clearDictsOfClient(client)
        except Exception:
            print("Closing Client without remove for: "+disconnectMessage)
        return user
    else:
        print("Closing Client for: "+disconnectMessage + ": Client was not logged in")
    client.close()
    return "unknown"

def initValidUsers(org = "ADPS"):
    userDir = org+"-Users/"
    workingDir = os.getcwd()
    dir = workingDir + "/MDC-Files/" + userDir
    try:
        change = os.listdir(dir)
        for user in change:
            splits = user.split(".")
            #print("User>" + splits[0])
            globals.AREUSERSLOGGEDIN[splits[0]] = False
            globals.VALIDUSERS.append(splits[0])
    except Exception:
        print("No Files Found in: "+dir)

def convertToString(bite):
    try:
        str = bite.decode("utf-8")
    except Exception:
        str = ""
    return str
def convertToBytes(str):
    byteStr = bytes(str, 'utf-8')
    return byteStr