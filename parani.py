import serial
import payloads # Contains encoded commands for scan execution

# Class is self-contained and only requires calls to internal methods
class Parani_SD1000:
    def __init__(self):
        # Params for connection to device
        self.serial_line = serial.Serial(
                port = "/dev/ttySerial",
                baudrate = 57600,
                write_timeout = None,
                timeout = 5
                )
        
        # Used for debugging purposes - stores byte stream
        self.response = None


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


    # Below methods were created before the PoC was functioning. Left for implementors understanding alone

    # Unnecessary for PoC, used during testing of device - was needed for bt_mode() method
    #def atz(self):
    #    self.serial_line.write(payloads.ATZ)
    #    self.response = self.serial_line.read(1000)
   
    # Unnecessary for PoC, part of rabbithole exploration about device - thought modes (0-3) were preventing command execution   
    #def bt_mode(self, mode: int):
    #    self.serial_line.write(payloads.BT_MODE[mode])
    #    self.response = self.serial_line.read(1000)
