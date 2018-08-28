from SocketScripts import SocketHelper as helper
import os
import socket


class SocketManage(object):

    def __init__(self):
        helper.initValidUsers()

    def testdata(self, data, client):
        if data:
            if (client not in helper.CONNECTIONS or helper.AREUSERSLOGGEDIN[helper.CONNECTIONS[client]] is False):
                isValidUser, user = self.checkIfLoggedIn(data)
            else:
                isValidUser = False
                user = ""
            if(isValidUser and not user == "Login"):
                helper.CONNECTIONS[client] = user
                helper.CLIENTIPS[user] = client
                print ("Logged in")
                print("   %s>> %s" % (helper.CONNECTIONS[client], data))
                client.send(helper.convertToBytes("Valid"))
            #if already logged in
            elif client in helper.CONNECTIONS and helper.AREUSERSLOGGEDIN[helper.CONNECTIONS[client]] is True:
                #sendto:badge:message
                if "sendto" in data.lower():
                    sending = data.split(":")
                    if sending[1] in helper.CLIENTIPS:
                        receiver = helper.CLIENTIPS[sending[1]]
                        receiver.send(helper.convertToBytes(sending[2]))
                        client.send(helper.convertToBytes("Valid"))
                        print("Valid Data")
                    else:
                        client.send(helper.convertToBytes("Invalid"))
                        print("Invalid Data")
                #get user list
                elif "userlist" in data.lower():
                    sending = "userlist"
                    for user in helper.VALIDUSERS:
                        if user is not "":
                            sending = sending+":"+user
                    client.send(helper.convertToBytes(sending))
                #get users online
                elif "loggedinusers" in data.lower():
                    sending = "usersonline"
                    for user in helper.CONNECTIONS:
                        if(helper.AREUSERSLOGGEDIN[user]):
                            sending = sending+":"+user
                    client.send(helper.convertToBytes(sending))
                else:
                    print("   %s>> %s" % (helper.CONNECTIONS[client], data))
                    client.send(helper.convertToBytes("rec"))
            #if user is logged on elsewhere
            else:
                try:
                    if(helper.AREUSERSLOGGEDIN[helper.CONNECTIONS[client]] is True):
                        print("Client already logged in")
                        helper.closingClient(client, "Already Logged in")
                except Exception:
                    print("Invalid Input")
                    helper.closingClient(client, "Invalid Input")
        else:
            helper.closingClient(client, "Disconnect")

    def checkIfLoggedIn(self,data):
        b = False
        #splitting = Badge:000000
        try:
            split = data.split(":")
            #is this a login attempt
            if(split[0].lower() == "badge"):
               for user in helper.VALIDUSERS:
                    #is it a valid user
                    if (split[1] == user and helper.AREUSERSLOGGEDIN[user] == False):
                        #if user is valid set as logged in
                        helper.AREUSERSLOGGEDIN[user] = True
                        b = True
                        break
                    else:
                        b = False
            else:
                return False, "invalid"
            return b, split[1]
        except:
            return False, "invalid"