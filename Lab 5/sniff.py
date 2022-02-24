from scapy.all import *
import numpy as np
import sqlite3 as lite

pkt_count = 1
pkt_group = list()
globalList = list()

def processGroup(pkt_group):
	global globalList
	pktLenList = list()
	for pkt in pkt_group:
		pktLenList.append(len(pkt))
	sumBytes = np.sum(pktLenList)
	mnLn = np.mean(pktLenList)
	sdLn = np.std(pktLenList)
	globalList.append([sumBytes, mnLn, sdLn])
	return ([sumBytes, mnLn, sdLn])


def pktHandler(pkt):
	global pkt_count, pkt_group
	pkt_count += 1
	pkt_group.append(pkt)
    
	if pkt_count % 10 == 0:
		groupId = pkt_count//10
		print("\npkt_count=",pkt_count)
		ftlist = processGroup(pkt_group)
		pkt_group = list()
		print('group Id {0} has features {1}'.format(groupId, ftlist))



if __name__ == '__main__':
    fname = 'dump.pcap'
    sniff(prn = pktHandler, offline=fname)