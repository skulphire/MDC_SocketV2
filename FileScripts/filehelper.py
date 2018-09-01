import os

workingdir = os.getcwd() + "/MDC-Files/"

def checkdirectory(directorytocheck, org="ADPS"):
    path = os.path.realpath(workingdir+org+"-"+directorytocheck)+"/"
    contents = os.listdir(path)
    newcontents = []
    for entry in contents:
        entry = entry.replace('[',"")
        entry = entry.replace(']', "")
        entry = entry.replace("'", "")
        newcontents.append(entry)
    return newcontents