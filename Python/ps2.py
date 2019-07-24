import psutil
from pymonad.Maybe import *

#
# Get list of running process sorted by Memory Usage
# https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage
#

def getProcessList():

    proclist = []

    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)

           # Append dict to list
           proclist.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
 
    # Sort list of dict by key vms i.e. memory usage
    proclist = sorted(proclist, key=lambda proc: proc['vms'], reverse=True)

    if len(proclist) > 0:
        return Just(proclist)
    else:
        return Nothing


print(getProcessList())
