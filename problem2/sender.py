from packet import packet
from reciever import reciever
import math
import numpy as np  

class sender:
    def send(self,inp,p_name,c_name):
        # print(len(inp))
        # print("jai shree ram")
        No_packets = len(inp)/7
        No_packets = math.ceil(No_packets)
        payload = np.empty(No_packets,dtype=object)

        print(No_packets)
        start = 0
        for i in range(No_packets):
            pkt = packet(p_name,c_name)
            pkt.id = i
            
            j = start
            while True:
                if j >= len(inp): break
                if len(pkt.message) > 7: break
                print(j)
                pkt.message += inp[j]
                j += 1    
                
            # print(pkt.message)
            # print(i)
            start += 8

            payload[i] = pkt
            
        reciever.recieve (payload)