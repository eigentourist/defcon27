import sys


def resolve(hostname):
    return '192.168.0.64'


def ping(ipaddr):
    return 42


def compose(g, f):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h


f = compose(ping, resolve)

responseTime = f('hostname')
print(f"Response time: {responseTime}")