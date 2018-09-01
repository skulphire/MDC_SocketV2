from SocketScripts import SocketHelper as helper
from SocketScripts import globals
from FileScripts import userfiles

class SocketManage(object):

    def testdata(self, data, client, server):
        if data:
            if (client not in globals.CONNECTIONS or globals.AREUSERSLOGGEDIN[globals.CONNECTIONS[client]] is False):
                isValidUser, user = self.checkIfValidUser(data)
            else:
                isValidUser = False
                user = ""
            if(isValidUser and not user == "Login"):
                globals.CONNECTIONS[client] = user
                globals.CLIENTIPS[user] = client
                print (user+" Has Logged in")
                print("   %s>> %s" % (globals.CONNECTIONS[client], data))
                client.send(helper.convertToBytes("Valid"))
            #if already logged in
            elif client in globals.CONNECTIONS and globals.AREUSERSLOGGEDIN[globals.CONNECTIONS[client]] is True:
                #sendto:badge:message
                if "sendto" in data.lower():
                    sending = data.split(":")
                    if(globals.AREUSERSLOGGEDIN[sending[1]]):
                        if sending[1] in globals.CLIENTIPS:
                            receiver = globals.CLIENTIPS[sending[1]]
                            receiver.send(helper.convertToBytes(sending[2]))
                            client.send(helper.convertToBytes("Valid"))
                            print("Valid Data")
                        else:
                            client.send(helper.convertToBytes("Invalid"))
                            print("Invalid Data")
                    else:
                        client.send(helper.convertToBytes("NoUser"))
                #get user list
                elif "userlist" in data.lower():
                    sending = "userlist"
                    for user in globals.VALIDUSERS:
                        if user is not "":
                            sending = sending+":"+user
                    client.send(helper.convertToBytes(sending))
                #get users online
                elif "loggedinusers" in data.lower():
                    sending = "usersonline"
                    for user in globals.VALIDUSERS:
                        print(user)
                        if(globals.AREUSERSLOGGEDIN[user]):
                            sending = sending+":"+user
                    client.send(helper.convertToBytes(sending))
                #issuper
                elif "issuper" in data.lower():
                    if(userfiles.checkIfSuper(globals.CONNECTIONS[client])):
                        client.send(helper.convertToBytes("True"))
                    else:
                        client.send(helper.convertToBytes("False"))
                #checkgt:gt
                elif "checkgt" in data.lower():
                    splits = data.split(":")
                    if(userfiles.checkGamerTag(globals.CONNECTIONS[client],splits[1])):
                        client.send(helper.convertToBytes("True"))
                    else:
                        client.send(helper.convertToBytes("False"))
                #getuseremail
                elif "getuseremail" in data.lower():
                    client.send(helper.convertToBytes(userfiles.getUserEmail(globals.CONNECTIONS[client])))
                elif "getuserrolename" in data.lower():
                    client.send(helper.convertToBytes(userfiles.getUserRoleName(globals.CONNECTIONS[client])))
                else:
                    print("   %s>> %s" % (globals.CONNECTIONS[client], data))
                    client.send(helper.convertToBytes("rec"))
            else:
                print("Invalid Input")
                helper.closingClient(client, "Invalid Input")
        else:
            helper.closingClient(client, "No Data (Crash)")

    def checkIfValidUser(self, data):
        print("Checking user..")
        b = False
        #splitting = Badge:000000
        try:
            split = data.split(":")
            #is this a login attempt
            if(split[0].lower() == "badge"):
                for user in globals.VALIDUSERS:
                    print(user)
                    #is it a valid user
                    if (split[1] == user and globals.AREUSERSLOGGEDIN[user] == False):
                        #if user is valid set as logged in
                        globals.AREUSERSLOGGEDIN[user] = True
                        b = True
                        break
                    else:
                        b = False
            else:
                return False, "invalid"
            return b, split[1]
        except Exception as e:
            print(e)
            return False, "invalid"