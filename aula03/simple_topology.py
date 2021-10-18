#!/usr/bin/python
from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi


def topology(remote_controller):
    "Create a network."
    net = Mininet_wifi()

    info("*** Adding stations/hosts\n")

    h1 = net.addHost("h1", ip="10.0.1.1", mac="00:00:00:00:01:01")
    h2 = net.addHost("h2", ip="10.0.1.2", mac="00:00:00:00:01:02")
    server1 = net.addHost("server1", ip="10.0.1.10", mac="00:00:00:00:01:0a")

    info("*** Adding P4Switches (core)\n")

    switch1 = net.addSwitch("switch1")

    info("*** Creating links\n")

    net.addLink(h1, switch1, bw=1000)
    net.addLink(h2, switch1, bw=1000)
    net.addLink(server1, switch1, bw=1000)

    info("*** Starting network\n")
    net.start()
    net.staticArp()

    info("*** Applying switches configurations\n")

    switch1.cmd("ovs-ofctl add-flow {} \"actions=output:NORMAL\"".format(switch1.name))

    info("*** Running CLI\n")
    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    remote_controller = False
    topology(remote_controller)
