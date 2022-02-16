import scapy.all as scapy
import numpy as np

def pkt_len():
    #make sure pcap file and python program are in the same directory
    pkts = scapy.rdpcap('dump.pcap')                                                                                                                        
    num_pkts = len(pkts)
    protocol = input("Enter protocol name:\n")
    pkt_lengths = []

    for i in range(num_pkts):
        pkt = pkts[i]
        if pkt.haslayer(protocol):
            pkt_lengths.append(len(pkt))
    
    print("\nNumber of packets having protocol as", protocol, "are: ", len(pkt_lengths))
    print("\nLengths of packets having protocol as", protocol, "are: ")
    print(pkt_lengths)

    mean = np.mean(pkt_lengths)
    std = np.std(pkt_lengths)

    print("\nMean packet length: ", mean)
    print("Standard Deviation: ", std)



if __name__ == "__main__":
    pkt_len()