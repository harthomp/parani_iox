from scapy.all import *
import socket

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
        StrFixedLenField("source_identifier", b"            ", 12), # Field for the MAC address payload
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

def raw_packet(packet) -> bytes:
    return raw(packet)

def send_packet_v1(packet):
    packet_v1 = IP(dst="192.168.1.2", src = "172.16.1.1")/UDP(dport = 2000, sport = RandShort())/packet
    send(packet_v1, iface = "eth0")
