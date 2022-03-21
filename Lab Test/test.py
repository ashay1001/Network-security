from scapy.all import *
import sqlite3 as lite

def createDB():
    dbname = 'master.db'
    conn = lite.connect(dbname)
    cursor = conn.cursor()
    tablename = 'wifiPacketFetures'
    stmt = 'Create table if not exists ' + tablename + '(id text,  timestamp text, addr1 text, addr2 text, addr3 text, addr4 text, Channel text, ChannelFrequency text, dBm_AntSignal text, proto text, type text, subtype text, len text, len_pkt text)'
    cursor.execute(stmt)
    conn.commit()

def wifiPacketFeatureExtractor(pkts):
    count = 0;
    pkts_len = len(pkts)
    dbname = 'master.db'
    conn = lite.connect(dbname)
    cursor = conn.cursor()
    tablename = 'wifiPacketFetures'
    stmt = 'insert into ' + tablename + ' (id, timestamp, addr1, addr2, addr3, addr4, Channel, ChannelFrequency, dBm_AntSignal, proto, type, subtype, len, len_pkt) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    for i in range(pkts_len):
        row = list()
        row.append(count)
        row.append(pkts[i].timestamp)
        row.append(pkts[i].addr1)
        row.append(pkts[i].addr2)
        row.append(pkts[i].addr3)
        row.append(pkts[i].addr4)
        row.append(pkts[i].Channel)
        row.append(pkts[i].ChannelFrequency)
        row.append(pkts[i].dBm_AntSignal)
        row.append(pkts[i].proto)
        row.append(pkts[i].type)
        row.append(pkts[i].subtype)
        row.append(pkts[i].len)
        row.append(len(pkts[i]))
        count += 1
        cursor.execute(stmt, row)
    
    conn.commit()
    print("\n Features stored inside DB.")




    




if __name__ == '__main__':
    pkts = rdpcap('smallDump.pcap')
    createDB()
    wifiPacketFeatureExtractor(pkts)