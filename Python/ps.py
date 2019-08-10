# Hacking With Monads:
# Functional Programming for the Blue Team
# A Def Con 27 Workshop August 10, 2019

# Get list of running process sorted by Memory Usage
# Small demonstration of lambda expressions
# https://thispointer.com/python-get-list-of-all-running-processes-and-sort-by-highest-memory-usage


import psutil


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


print(getProcessList())
