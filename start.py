import os
from time import sleep

tokens = open("tokens.txt", "r").read().split("\n")
code = open("code.txt", "r").read()
serverid = input("Server ID > ")
serverinvitecode = input("Server invite code > ")
message = input("Message > ")

for i in range(len(tokens)):
    file = open(f"spam{i}.py", "w")
    file.write(code.replace("48", serverid).replace("36", tokens[i]).replace("34", message).replace("32", serverinvitecode))
    file.close()

for i in range(len(tokens)):
    os.startfile(f"spam{i}.py")

sleep(30)
for i in range(len(tokens)):
    os.remove(f"spam{i}.py")