# ######################################################################################
# --------------------------------------------------------------------------------------
# !! This is a script writen by brahim bellaoui the extended version can be found
# either on the owner github or by contacting him by email bellaouibrahim6@gmail.com.
# Enjoy .. :)
# --------------------------------------------------------------------------------------
# ######################################################################################



# ----------------------------------- DESCRIPTION --------------------------------------

# This script models the basic black-box that represents "admin controller" module within
# the PoC chain of IaaS server controling in the Healthcare Data Hosting norms (a.k.a
# HDS datas).

# the box has two inputs coming from the probes installed on instances in the client
# tenants : instance address, message
# "instance address" : this value allows to uniquely identify the instance and then
# retrieve its ID (the IDs within OpenStack are external informations; the instance
# does not have any idea about the upstream informations)
# "message" : this message reflectes either the behavior within the instance is allowed
# by HDS norm or not.

# the output of the box is an interaction with the compute server (in this case Nova
# Compute). And this in the case of required action to perform depending on the critica-
# lity of the abnormal behavior within the instance.

# the core of the box is following the algorithm below:
#
# - Get intance address (ins_addr) and the message (in_msg)
# - Authenticate to the NovaClient API
# - Retrieve instance ID (mapping cross servers.list(all-tenants option) and ins_addr)
# - Figure out the action to perfom depending on in_msg
# - Send request the nova compute via NovaClient API
# - Print the answer and trace the process.

# ######################################################################################



# --------------------------------------------------------------------------------------

#
#

# ######################################################################################

# ------------------------------------ IMPORTANT ---------------------------------------

# This script needs to be joined with other Python files; to be listed :
#
# - credentials.py
# -
#

# ######################################################################################


# ######################################################################################
# ------------------------------------ THE CORE ----------------------------------------
# ######################################################################################

#!/usr/bin/env python
from credentials import get_nova_credentials_v2
from novaclient.client import Client

# Get the instance address
# addr = ins_addr
#
#
credentials = get_nova_credentials_v2()
nova_client = Client(**credentials)

instances = nova_client.servers.list(search_opts={'all_tenants':1})


print 'No', '   ID', '  Name', '        Status'
i = 1
for instance in instances:
        if i==1:
                print 'No', 'ID', 'Name', 'Status'
        print i, instance.id, instance.name, instance.status, instance.networks.values()
        if instance.networks.values()=="[[u'10.0.1.8']]":
               print 'yaaa that is it'
        else:
                print 'sorry not now'
        i+=1



