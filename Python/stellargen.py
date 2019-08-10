# Hacking With Monads:
# Functional Programming for the Blue Team
# A Def Con 27 Workshop August 10, 2019

# Demo of generators and coroutines


import sys

elements = ['hydrogen', 'helium', 'carbon', 'neon', 'oxygen', 'silicon', 'iron']

# Generator
def core_evolve():
    print('Initializing stellar core')
    for elem in elements:
        msg = elem
        if elem == 'silicon':
            msg = elem + '   ** Warning: Supernova imminent'
        elif elem == 'iron':
            msg = elem + '   ** SUPERNOVA EXPLOSION **'
        yield msg

# Generator Coroutine
def core_status():
    print('Initializing status')
    while True:
        elem = (yield)
        if elem in elements:
            if elem == 'silicon':
                print('** Warning: Supernova Imminent **')
            elif elem == 'iron':
                print('*** SUPERNOVA EXPLOSION ***')
            else:
                print('Status nominal')
        else:
            print('Substance not found, status nominal')
