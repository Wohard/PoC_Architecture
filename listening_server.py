#import admin_controller
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("0.0.0.0", 48769),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.

#server.register_function(pow)

# Register a function under a different name
#def adder_function(x,y):
#    return x + y
#server.register_function(adder_function, 'add')

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').
#class MyFuncs:
#    def div(self, x, y):
#        return x // y

#server.register_instance(MyFuncs())

#


# Resister the function to be called "admin_controller.py"

from credentials import get_nova_credentials_v2
from novaclient.client import Client
import sys
# Get the instance address 
# addr = ins_addr
# 
#
credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

instances = nova_client.servers.list(search_opts={'all_tenants':1})

# 
def admin_controller(message, address):
	msg = message       # msg_warning
	ins_addr = address  # 10.0.1.7

	if msg == 'msg_ok':
		print 'safety confirmation has been received from ', ins_addr
	elif msg == 'msg_warning':
		for instance in instances:
			if instance.networks.values()[0][0]==ins_addr:
				print '='*60
				print '*'*15,' HDS Vulnerability warning ', '*'*16
				print '='*60
				print '\n'
                		print instance.id, instance.name, instance.status, instance.networks.values()[0][0]
				print 'the instance', instance.name, ' has an abnormal behavior'
				print 'the appropriate action is in process'
				instance.unpause()
				print 'DONE'
				ID_ins = instance.id
#			
			else:
				print 'khokho n tazart'



server.register_function(admin_controller, 'probe')





# Run the server's main loop
server.serve_forever()

"""
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8769')
print s.pow(2,3)  # Returns 2**3 = 8
print s.add(2,3)  # Returns 5
print s.div(5,2)  # Returns 5//2 = 2

# Print list of available methods
print s.system.listMethods()

"""
