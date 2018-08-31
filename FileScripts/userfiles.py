import os

def checkIfSuper(user,org="ADPS"):
    workingdir = os.getcwd()
    filedir = workingdir + "/MDC-Files/" + org+"-Users/"
    print("File Dir: "+filedir)
    if(user in filedir):
        with open(user) as f:
            lines = f.readlines()
        if("Super" in lines[1]):
            return True
    else:
        print("User does not exist")
        return False
#def checkGamerTag(user,org="ADPS"):
