from scapy.all import *
import numpy as np
import sqlite3 as lite

pkt_count = 0
pkt_group = list()
globalList = list()

def storeInDb():
    global globalList
    dbname = 'Demo1.db'
    conn = lite.connect(dbname)
    cursor = conn.cursor()
    tablename = 'features'
    stmt = 'Create table if not exists ' + tablename + '( GroupId integer, sumPktLen integer, mnPktLen float, sdPktLen float)'
    cursor.execute(stmt)
    conn.commit()
    group_count = len(globalList)
    for i in range(group_count):
        ftlist = ()
        ftlist = globalList[i]
        stmt = 'insert into ' + tablename + ' (GroupId, sumPktLen, mnPktLen, sdPktLen) values(?,?,?,?)'
        cursor.execute(stmt, ftlist)
    conn.commit()
    conn.close()

def processGroup(groupId ,pkt_group):
    global globalList
    pktLenList = list()
    for pkt in pkt_group:
        pktLenList.append(len(pkt))
    pktsum = np.sum(pktLenList)
    mnLn = np.mean(pktLenList)
    sdLn = np.std(pktLenList)
    globalList.append([groupId,pktsum, mnLn, sdLn])


def pktHandler(pkt):
    if pkt.haslayer("UDP"):
        global pkt_count, pkt_group
        pkt_count += 1
        pkt_group.append(pkt)
        
        if pkt_count % 10 == 0:
            groupId = pkt_count//10
            processGroup(groupId ,pkt_group)
            pkt_group = list()



if __name__ == '__main__':
    fname = 'dump.pcap'
    sniff(prn = pktHandler, offline=fname)
    storeInDb()
    print("Required Values inserted into table")