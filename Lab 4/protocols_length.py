from asyncio import protocols
from typing import Protocol
import scapy.all as scapy
import numpy as np

def get_packet_layers(packet):
    counter = 0
    while True:
        layer = packet.getlayer(counter)
        if layer is None:
            break

        yield layer
        counter += 1

def getProtocols():
    pkts = scapy.rdpcap('dump.pcap')
    number_pkts = len(pkts)
    protocols_dict = {}
    
    for i in range(number_pkts):
        for layer in get_packet_layers(pkts[i]):
            if protocols_dict.__contains__(layer.name):
                protocols_dict[layer.name].append(len(pkts[i]))
            else:
                protocols_dict[layer.name] = [len(pkts[i])]
    
    return protocols_dict

if __name__ == "__main__":

   #below dictionary contains all the protocols as keys and list of packet lengths 
   protocols_dict =  getProtocols()

   for key in protocols_dict:
       pkts = protocols_dict[key]
       mean = np.mean(pkts)
       std = np.std(pkts)
       print("Protocol:", key)
       print("Number of packets:", len(pkts), "\tMean packet length:", np.round(mean, 2), "\tStandard Deviation:", np.round(std, 2))
       print("\n")
   

   