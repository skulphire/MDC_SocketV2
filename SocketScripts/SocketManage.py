from SocketScripts import SocketHelper as helper
import os
import socket


class SocketManage(object):

    def __init__(self):
        org = "ADPS"
        self.userDir = org+"-Users/"
        self.areUsersLoggedIn = {}
        self.connections = {}
        self.clientIP = {}
        try:
            workingDir = os.getcwd()
            dir = workingDir+"/MDC-Files/"+self.userDir
            self.validUsers = os.listdir(dir)
            for user in self.validUsers:
                #print("User>"+user)
                self.areUsersLoggedIn[user] = False
        except Exception:
            print("no files found")

    def testdata(self, data, client):
        while True:
            if data:
                if (client not in self.connections or self.areUsersLoggedIn[self.connections[client]] is False):
                    isValidUser, user = self.checkIfLoggedIn(data)
                else:
                    isValidUser = False
                    user = ""
                if(isValidUser and not user == "Login"):
                    self.connections[client] = user
                    self.clientIP[user] = client
                    print ("Logged in")
                    print("   %s>> %s" % (self.connections[client], data))
                    client.send(helper.convertToBytes("Valid"))
                #if already logged in
                elif client in self.connections and self.areUsersLoggedIn[self.connections[client]] is True:
                    #sendto:badge:message
                    if "sendto" in data.lower():
                        sending = data.split(":")
                        if sending[1] in self.clientIP:
                            receiver = self.clientIP[sending[1]]
                            receiver.send(helper.convertToBytes(sending[2]))
                            client.send(helper.convertToBytes("Valid"))
                            print("Valid Data")
                        else:
                            client.send(helper.convertToBytes("Invalid"))
                            print("Invalid Data")
                    #get user list
                    elif "userlist" in data.lower():
                        sending = "userlist"
                        for user in self.validUsers:
                            if user is not "":
                                sending = sending+":"+user
                        client.send(helper.convertToBytes(sending))
                    #get users online
                    elif "loggedinusers" in data.lower():
                        sending = "usersonline"
                        for user in self.connections:
                            if(self.areUsersLoggedIn[user]):
                                sending = sending+":"+user
                        client.send(helper.convertToBytes(sending))
                    else:
                        print("   %s>> %s" % (self.connections[client], data))
                        client.send(helper.convertToBytes("rec"))
                #if user is logged on elsewhere
                else:
                    try:
                        if(self.areUsersLoggedIn[self.connections[client]] is True):
                            print("Client already logged in")
                            self.closingClient(client, "Already Logged in")
                            break
                    except:
                        continue
            else:
                print("no")
                self.closingClient(client, "Disconnect")
                break

    def clearDictsOfClient(self,client):
        print("Removing user")
        self.areUsersLoggedIn[self.connections[client]] = False
        del self.clientIP[client]
        del self.connections[client]
    def closingClient(self,client,disconnectMessage):
        if(client in self.clientIP):
            try:
                print("Closing "+self.connections[client]+"for: "+disconnectMessage)
                self.clearDictsOfClient(client)
            except Exception:
                print("Closing Client for: "+disconnectMessage)
        else:
            print("Closing Client for: "+disconnectMessage)
        client.close()

    def checkIfLoggedIn(self,data):
        b = False
        #splitting = Badge:000000
        try:
            split = data.split(":")
            #is this a login attempt
            if(split[0].lower() == "badge"):
               for user in self.validUsers:
                    #is it a valid user
                    if (split[1] == user and self.areUsersLoggedIn[user] == False):
                        #if user is valid set as logged in
                        self.areUsersLoggedIn[user] = True
                        b = True
                        break
                    else:
                        b = False
            else:
                return False, "invalid"
            return b, split[1]
        except:
            return False, "invalid"