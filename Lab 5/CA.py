from scapy.all import *
import numpy as np

pkt_count = 0
globalList = list()


def pktHandler(pkt):
    global pkt_count, globalList
    
    if pkt.haslayer("UDP"):
        pkt_count += 1
        globalList.append(len(pkt))



if __name__ == '__main__':
    fname = 'dump.pcap'
    sniff(prn = pktHandler, offline=fname)
    pktsum = np.sum(globalList)
    pktmean = np.mean(globalList)
    pktsd = np.std(globalList)
    print("Count of UDP Packets: ", pkt_count)
    print("Sum: ", pktsum, "\tMean: ", pktmean, "\tStandard Deviation: ", pktsd)