import os

workingdir = os.getcwd() + "/MDC-Files/"

def checkADPSdirectory(directorytocheck, org="ADPS"):
    try:
        path = os.path.realpath(workingdir+org+"-"+directorytocheck)+"/"
        contents = os.listdir(path)
        newcontents = ""
        for entry in contents:
            #print("Dir contents: "+entry)
            splits = entry.split(".")
            newcontents = newcontents +splits[0] +","
        return newcontents
    except Exception as e:
        print(e)
        return "none"
def checkReportsdirectory(folder,org="ADPS"):
    path = os.path.realpath(workingdir+org+"-ReportDatabase/"+folder)+"/"
    contents = os.listdir(path)
    newcontents = ""
    for entry in contents:
        splits = entry.split(".")
        newcontents = newcontents+splits[0]+","
    return newcontents

def getReport(folder,file, org="ADPS"):
    path = os.path.realpath(workingdir + org + "-ReportDatabase/" + folder) + "/"
    file = file+".txt"
    try:
        send = ""
        with open(path+file) as f:
            lines = f.readlines()
        for line in lines:
            send = send+line+","
        return send
    except Exception as e:
        print(e)
        return "none"
def getSuspect(file, org="ADPS"):
    path = os.path.realpath(workingdir + org + "-SuspectDatabase") +"/"
    #file = file + ".txt"
    print("get Suspect filename: "+file)
    try:
        send = ""
        with open(path + file) as f:
            lines = f.readlines()
        for line in lines:
            send = send + line + ","
        return send
    except Exception as e:
        print(e)
        return "none"
def newsuspect(filename,data,org="ADPS"):
    path = os.path.realpath(workingdir + org + "-SuspectDatabase") + "/"
    try:
        with open(path+filename) as f:
            #f.writelines()
