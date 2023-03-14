#This is a Port Scanner Primarily Written in Python and works on both Windows and Linux
import pyfiglet
import sys
import socket
from datetime import datetime

ascli_banner = pyfiglet.figlet_format("Port Scanner")
print(ascli_banner)

#Defining the Target
if len(sys.argv) == 2:
    #Translate Hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of Argument")
    print("Syntax: python3 scanner.py <ip>")
#Add a Banner 
print("-" * 50)
print("Scanning Target " + target)
print("Scanning Started at " + str(datetime.now()))
print("-" * 50)

try:
    #This will scan ports between 1 to 65,535
    for port in range(1,65535): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        # returns an error messages
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("Exiting Program")
    sys.exit()
except socket.gaierror:
    print("Hostname Could Not Be Resolved")
    sys.exit()

except socket.error:
    print("Couldn't Connect to Server")
    sys.exit()