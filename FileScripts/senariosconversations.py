import os
import random

workingdir = os.getcwd() + "/MDC-Files/Senarios/Conversations/"

def readScript(script):
    try:
        path = os.path.realpath(workingdir+script+".txt")
        with open(path) as f:
            count = 0
            for line in f:
                count=count+1
            rnd = random.randint(0,count)
            lines = f.readlines()
        return lines[rnd]
    except Exception as e:
        print(e)
        return "Exception"