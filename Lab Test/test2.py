from scapy.all import *
import sqlite3 as lite

def createDB():
    dbname = 'master.db'
    conn = lite.connect(dbname)
    cursor = conn.cursor()
    tablename = 'wifiPacketFetures'
    stmt = 'Create table if not exists ' + tablename + '(id text,  timestamp text, addr1 text, addr2 text, addr3 text, addr4 text, Channel text, ChannelFrequency text, dBm_AntSignal text, proto text, type text, subtype text, len text, len_pkt text)'
    cursor.execute(stmt)
    tablename = 'assocPacketFeatures'
    stmt = 'Create table if not exists ' + tablename + '(id text,  timestamp text, addr1 text, addr2 text, addr3 text, addr4 text, Channel text, ChannelFrequency text, dBm_AntSignal text, proto text, type text, subtype text, len text, len_pkt text, SC text, fcs text, listen_interval text, cipher text, oui text, Vendorid text, Vendoroui text)'
    tablename = 'm1PacketFeatures'
    stmt = 'Create table if not exists ' + tablename + '(id text,  timestamp text, addr1 text, addr2 text, addr3 text, addr4 text, Channel text, ChannelFrequency text, dBm_AntSignal text, proto text, type text, subtype text, len text, len_pkt text, SC text, fcs text, oui text)'
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



def assocPacketFeatures(pkts):
    dbname = 'master.db'
    conn = lite.connect(dbname)
    cursor = conn.cursor()
    tablename = 'assocPacketFeatures'
    stmt = 'insert into ' + tablename + ' (id, timestamp, addr1, addr2, addr3, addr4, Channel, ChannelFrequency, dBm_AntSignal, proto, type, subtype, len, len_pkt, SC, fcs, listen_interval, cipher, oui, Vendorid, Vendoroui) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    count = 0
    pkt_len = len(pkts)
    for i in range(pkt_len):
        row = []
        if(pkts[i].type == 0 and (pkts[i].subtype == 0 or pkts[i].subtype == 1)):
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
            row.append(pkts[i].SC)
            row.append(pkts[i].fcs)
            if(pkts[i].subtype == 0):
                row.append(pkts[i].listen_interval)
                row.append(pkts[i][Dot11EltRSN].group_cipher_suite[RSNCipherSuite].cipher)
                row.append(pkts[i][Dot11EltRSN].group_cipher_suite[RSNCipherSuite].oui)
            else:
                row.append(None)
                row.append(None)
                row.append(None)
            #row.append(pkts[i][Dot11EltRates].rates)
            if(pkts[i].subtype == 1):
                row.append(pkts[i][Dot11EltVendorSpecific].ID)
                row.append(pkts[i][Dot11EltVendorSpecific].oui)
            else:
                row.append(None)
                row.append(None)
            count += 1
            cursor.execute(stmt, row)
    conn.commit()
    print("\n Features from association request/response frame inserted into DB")
    

    




if __name__ == '__main__':
    pkts = rdpcap('master.pcap')
    createDB()
    wifiPacketFeatureExtractor(pkts)
    assocPacketFeatures(pkts)