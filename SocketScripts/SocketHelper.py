import os

#GLOBALS
VALIDUSERS = []
AREUSERSLOGGEDIN = {}
CONNECTIONS = {}
CLIENTIPS = {}


def clearDictsOfClient(client):
    print("Removing user")
    AREUSERSLOGGEDIN[CONNECTIONS[client]] = False
    del CLIENTIPS[client]
    del CONNECTIONS[client]

def closingClient(client,disconnectMessage):
    if(client in CLIENTIPS):
        try:
            print("Closing "+CONNECTIONS[client]+"for: "+disconnectMessage)
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
        VALIDUSERS = os.listdir(dir)
        for user in VALIDUSERS:
            print("User>"+user)
            AREUSERSLOGGEDIN[user] = False
    except Exception:
        print("No Files Found in: "+dir)

def convertToString(bite):
    str = bite.decode("utf-8")
    return str
def convertToBytes(str):
    byteStr = bytes(str, 'utf-8')
    return byteStr