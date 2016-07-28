from mininet.node import Controller
from os import environ

FLDIR = environ['HOME'] + '/floodlight'
print(FLDIR)


class Floodlight(Controller):
    def __init__(self, name, cdir=FLDIR,
                 command='java -jar target/floodlight.jar',
                 cargs=(),
                 port=6653,
                 ip='192.168.1.1',
                 **kwargs):
        Controller.__init__(self, name, cdir=cdir,
                            command=command,
                            cargs=cargs, port=port, ip=ip, **kwargs)
