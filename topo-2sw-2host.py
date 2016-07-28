"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from floodlight import Floodlight
import os
import sys


def simpleTest():
    """Create and test a simple network"""
    net = Mininet(topo=None, build=False)

    # Add hosts
    print("Adding hosts...")
    h1 = net.addHost('h1', ip='20.0.0.1/24')
    h2 = net.addHost('h2', ip='30.0.0.1/24')

    # Add switches
    print("Adding switches...")
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    # Add links
    print("Adding links...")
    net.addLink(h1, s1)
    net.addLink(s1, s2)
    net.addLink(s2, h2)

    # Add controllers
    print("Adding controllers...")
    fl0 = Floodlight('fl0', cargs=('-cf src/main/resources/floodlightmininet_1.properties'), ip='192.168.1.1', port=6653)
    #c0 = net.addController(name='c0', controller=fl0)
    fl1 = Floodlight('fl1', cargs=('-cf src/main/resources/floodlightmininet_2.properties'), ip='192.168.2.1', port=7653)
    #c1 = net.addController(name='c1', controller=fl1)


    print("Building network...")
    net.build()

    print("Starting controllers...")
    #s1.start([c0])
    #s2.start([c1])

    CLI(net)
    net.stop()


    if __name__ == '__main__':
        # Tell mininet to print useful information
        setLogLevel('info')

if os.geteuid() != 0:
    print("*** sudo python " + sys.argv[0] + " ***")
    os.execvp("sudo", ["sudo"] + ["python"] + sys.argv)
simpleTest()
