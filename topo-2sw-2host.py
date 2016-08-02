"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininext.net import MiniNExT as Mininext
from mininext.services.quagga import QuaggaService
from floodlight import Floodlight
import os
import sys


def simpleTest():
    """Create and test a simple network"""
    net = Mininext(topo=None, build=False)

    "Initialize a service helper for Quagga with default options"
    quaggaSvc = QuaggaService(autoStop=False)

    # Add controllers
    print("Adding controllers...")
    c0 = net.addController(name='c0', controller=Floodlight, ip='127.0.0.1', port=6653,
                           cargs='-cf src/main/resources/floodlightmininet_1.properties')
    c1 = net.addController(name='c1', controller=Floodlight, ip='127.0.0.1', port=7653,
                           cargs='-cf src/main/resources/floodlightmininet_2.properties')

    print("Adding switches...")
    switch1 = net.addSwitch('switch1')
    switch2 = net.addSwitch('switch2')

    print("Adding hosts...")
    host1 = net.addHost('host1', ip='10.0.0.1/24')
    host2 = net.addHost('host2', ip='20.0.0.1/24')

    print("Adding links...")
    net.addLink(host1, switch1)
    net.addLink(host2, switch2)
    net.addLink(switch1, switch2)

    print("Building network...")
    print(net.hosts)
    net.build()

    print("Starting controllers...")
    for controller in net.controllers:
        controller.start()

    print("Starting switches...")
    net.get('switch1').start([c0])
    net.get('switch2').start([c1])

    CLI(net)
    net.stop()

    if __name__ == '__main__':
        # Tell mininet to print useful information
        setLogLevel('info')


if os.geteuid() != 0:
    print("*** sudo python " + sys.argv[0] + " ***")
    os.execvp("sudo", ["sudo"] + ["python"] + sys.argv)
simpleTest()
