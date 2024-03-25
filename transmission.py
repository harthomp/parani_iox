from scapy.all import *
from datetime import datetime, timezone

#https://scapy.readthedocs.io/en/latest/build_dissect.html
class IncomingMessageProtocol(Packet):
    name = "AddInsight IMPv1"
    fields_desc = [
        # Header fields
        XByteField("signature", 0), # Type of probe
        BitField("source_identifier_type", 0, 6), # Type of data
        
        # Payload
        BitField("has_ibeacon", 0, 1), # Shows if Outgoing Message Protocol supported
        XBitField("padding1", 0, 1), 
        BitField("low_byte_asset_number", 0, 8),  # Used for the internal hardware asset value
        BitField("high_byte_asset_number", 0, 8), # Together range of 0 - 65535, i.e. low set to 0xFF and high to 0x00 would be asset num 255, 99% sure this is how it works. - True
        StrLenField("source_identifier", None, max_length = 12), # Field for the MAC address payload
        XBitField("padding2", 0, 1),
        
        # Fields relate to timestamping - ten_x relate to the tenths of that value
        BitField("ten_seconds", 0, 3),
        BitField("seconds", 0, 4),
        XBitField("padding3", 0, 1),
        BitField("ten_minutes", 0, 3),
        BitField("minutes", 0, 4),
        XBitField("padding4", 0, 2),
        BitField("ten_hour", 0, 2),
        BitField("hours", 0, 4),
        XBitField("padding5", 0, 2),
        BitField("ten_date", 0, 2),
        BitField("date", 0, 4),
        BitField("is_utc", 1, 1),
        XBitField("padding6", 0, 2),
        BitField("ten_month", 0, 1),
        BitField("month", 0, 4),
        BitField("ten_year", 0, 4),
        BitField("year", 0, 4)
        ]

def tenths_time(time: int): return (time // 10) % 10
def oneths_time(time: int): return time % 10

            #source_identifier = mac_addr,
            #ten_seconds =  tenths_time(timestamp.second),
            #seconds = oneths_time(timestamp.second),
            #ten_minutes = tenths_time(timestamp.minute),
            #minutes = oneths_time(timestamp.minute),
            #ten_hour = tenths_time(timestamp.hour),
            #hours = oneths_time(timestamp.hour),
            #ten_date = tenths_time(timestamp.day),
            #date = oneths_time(timestamp.day),
            #ten_month = tenths_time(timestamp.month),
            #month = oneths_time(timestamp.month),
            #ten_year = tenths_time(timestamp.year - 2000),
            #year = oneths_time(timestamp.year - 2000)
            #)    
    #print(packet.show())
    
    # Can also be done by appending to UDP()/IncomingMessageProtocolV1(signature = y, source_id_type = x, etc)
    #packet_v1 = IP(dst="10.66.227.88", src = "123.123.123.123")/UDP(dport = 2000, sport = RandShort())/packet


    #return raw(x)
