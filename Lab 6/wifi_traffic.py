from scapy.all import *


def filter_pkt():
    pkt_pcap = rdpcap('dump_test.pcap')
    print(pkt_pcap[13][Dot11][Dot11FCS].type)

    pkt_lst = list()
    for pkt in pkt_pcap:
        if pkt[Dot11][Dot11FCS].type == 0 and pkt[Dot11][Dot11FCS].subtype == 8:
            pkt_lst.append(pkt)

    print(len(pkt_lst))







if __name__ == '__main__':
    filter_pkt()