from mininet.moduledeps import pathCheck
from mininet.node import Controller
from os import environ

FLDIR = environ['HOME'] + '/floodlight'

class Floodlight(Controller):
    def __init__(self, name, cdir=FLDIR,
                 command='java -jar target/floodlight.jar',
                 cargs='',
                 ip='127.0.0.1',
                 port=6653,
                 **kwargs):
        Controller.__init__(self, name, cdir=cdir,
                            command=command,
                            cargs=cargs, ip=ip, port=port, **kwargs)

    def start(self):
        """Start <controller> <args> on controller.
           Log to /tmp/cN.log"""
        pathCheck(self.command)
        cout = '/tmp/' + self.name + '.log'
        if self.cdir is not None:
            self.cmd('cd ' + self.cdir)
        # print(self.command + ' ' + self.cargs +
        #          ' 1>' + cout + ' 2>' + cout + '&')
        self.cmd(self.command + ' ' + self.cargs +
                 ' 1>' + cout + ' 2>' + cout + '&')
        self.execed = False
