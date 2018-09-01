import os
import random

workingdir = os.getcwd() + "/MDC-Files/Senarios/Conversations/"

def readScript(script):
    try:
        path = os.path.realpath(workingdir+script+".txt")
        with open(path) as f:
            count = 0
            lines = f.readlines()
            count = len(lines)
            rnd = random.randint(0,count)
        return lines[rnd].strip('\n')
    except Exception as e:
        print(e)
        return "Exception"