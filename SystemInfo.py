# Python program to find system information
import sys
import socket
import os
import platform

print  "Name: " +socket.gethostname()
print "FQDN: " +socket.getfqdn()
print "System Platform: "+sys.platform
print "Machine: " +platform.machine()
print "Node " +platform.node()
print "Platform: "+platform.platform()
print "Pocessor: " +platform.processor()
print "System OS: "+platform.system()
print "Release: " +platform.release()
print "Version: " +platform.version()
