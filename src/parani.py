import serial
import os
import payloads # Contains encoded commands for scan execution
from datetime import datetime, timezone
import transmission

# Used for setting packet parameters
def tenths_time(time: int): return (time // 10) % 10
def oneths_time(time: int): return time % 10

# Class is self-contained and only requires calls to internal methods
class Parani_SD1000:
    def __init__(self):
        # Params for connection to device
        self.serial_line = serial.Serial(
                port = os.getenv("IR_SERIAL", "/dev/ttySerial"), # Stolen from github.com/etychon/iox-ir1101-serial-port
                baudrate = 57600,
                write_timeout = None,
                timeout = 0.1
                )

        # Used for debugging purposes - stores byte stream
        self.response = None
        self.response_tuples: list(tuple(str, datetime)) = []

        self.packet: transmission.IncomingMessageProtocol = None

    # 1000 bytes used for read param now as unsure of sizing reqs. 

    # Returns byte stream containing device info
    def bt_info(self):
        self.serial_line.write(payloads.BT_INFO)
        self.response = self.serial_line.read(1000)

    # Performs scanning functionality, left as default for now - refer to doc for possible S register change
    def bt_inq(self):
        self.serial_line.write(payloads.BT_INQ)
        self.response = self.serial_line.read(1000)
    
    # Necessary for turning operational status of device from PENDING to STANDBY - can return ERROR or OK, just needs to run before executing bt_inq() method
    def bt_cancel(self):
        self.serial_line.write(payloads.BT_CANCEL)
        self.response = self.serial_line.read(1000)

    def flush_buffer(self):
        self.serial_line.flush()

    def ats_s4(self):
        self.serial_line.write(payloads.ATS_S4)

    def ats_s33(self):
        self.serial_line.write(payloads.ATS_S33)

    def set_s_registers(self):
        self.ats_s4()
        self.ats_s33()

    def bt_inq_readline(self):
        self.serial_line.write(payloads.BT_INQ)
        
        # Clear tuple list so doesn't compound over time
        self.response_tuples.clear()
        
        x: str = None
        while True:
            x = self.serial_line.readline()
            if x != b"OK\r\n": 
                if x != b"\r\n" and x != b"" and x != b"ERROR\\r\\n" and x != b"ERROR\r\n":
                    x = x.split(b",")
                    self.response_tuples.append((x[0], datetime.now(timezone.utc)))
            else:
                break

    def set_packet_parameters(self, mac_addr, timestamp):
        self.packet = transmission.IncomingMessageProtocol(
                    signature = 0xEE,
                    source_identifier_type = 60,
                    has_ibeacon = 0,
                    low_byte_asset_number = 0xFF,
                    high_byte_asset_number = 0x00,
                    source_identifier = mac_addr,
                    ten_seconds = tenths_time(timestamp.second),
                    seconds = oneths_time(timestamp.second),
                    ten_minutes = tenths_time(timestamp.minute),
                    minutes = oneths_time(timestamp.minute),
                    ten_hour = tenths_time(timestamp.hour),
                    hours = oneths_time(timestamp.hour),
                    ten_date = tenths_time(timestamp.day),
                    date = oneths_time(timestamp.day),
                    ten_month = tenths_time(timestamp.month),
                    month = oneths_time(timestamp.month),
                    ten_year = tenths_time(timestamp.year - 2000),
                    year = oneths_time(timestamp.year - 2000)
                )
