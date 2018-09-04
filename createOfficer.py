import os

print("Welcome! Use this to create new users for your MDC System")
workingdir = os.getcwd()
org = input("Organization: ")
filedir = workingdir + "/MDC-Files/" + org+"-Users/"
real = os.path.realpath(filedir)+"/"
again = True
while again:
    badge = input("User badge number (This will be used to login to the system: ")
    filename = badge+".txt"
    rolename = input("User Roleplay name: ")
    email = input("User email (input 'none' if not applicable): ")
    gamertag = input("Enter User Windows Live Gamertag exactly: ")
    super = input("Is User a Supervisor? (Y/N) :")
    if("yes" or "y" in super.lower()):
        super = "Super"
    else:
        super = "notsuper"

    print("Creating user...")
    with open(real+filename, 'w') as f:
        f.write(rolename+'\n'+email+'\n'+gamertag+'\n'+super+'\n')
    print("User created")
    another = input("Add another user? (Y/N) :")
    if("y" in another):
        again = True
    else:
        again = False