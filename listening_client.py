
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:48769') # the address of the server 
#print s.pow(2,3)  # Returns 2**3 = 8
#print s.add(2,3)  # Returns 5
#print s.div(5,2)  # Returns 5//2 = 2
s.probe("msg_ok", "10.0.1.7")
# Print list of available methods
#print s.system.listMethods()
