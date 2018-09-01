import os

def checkIfSuper(user,org="ADPS"):
    user = user+".txt"
    workingdir = os.getcwd()
    filedir = workingdir + "/MDC-Files/" + org+"-Users/"
    #print("File Dir: " + filedir)
    try:
        filedirlist = os.listdir(filedir)
        print(filedirlist)
        if (user in filedirlist):
            with open(user) as f:
                lines = f.readlines()
            if ("Super" in lines[3]):
                return True
        else:
            print("User does not exist")
            return False
    except Exception as e:
        print(e)
        return False

def checkGamerTag(user, gamertag,org="ADPS"):
    user = user + ".txt"
    workingdir = os.getcwd()
    filedir = workingdir + "/MDC-Files/" + org + "-Users/"
    #print("File Dir: " + filedir)
    try:
        filedirlist = os.listdir(filedir)
        if (user in filedirlist):
            with open(user) as f:
                lines = f.readlines()
            if (gamertag in lines[2]):
                return True
        else:
            print("User does not exist")
            return False
    except Exception as e:
        print(e)
        return False

def getUserEmail(user,org="ADPS"):
    user = user + ".txt"
    workingdir = os.getcwd()
    filedir = workingdir + "/MDC-Files/" + org + "-Users/"
    #print("File Dir: " + filedir)
    try:
        filedirlist = os.listdir(filedir)
        if (user in filedirlist):
            with open(user) as f:
                lines = f.readlines()
                if("none" or "@" in lines[1]):
                    return lines[1]
                else:
                    return "none"
        else:
            print("User does not exist")
            return "none"
    except Exception as e:
        print(e)
        return "none"