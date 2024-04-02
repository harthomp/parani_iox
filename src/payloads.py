from conf import Config

# Command list in Appendix B of below link
# https://microtechnica.tv/support/manual/sd1000_man.pdf
 
ATZ = "ATZ\r".encode("utf-8")

BT_INFO = "AT+BTINFO?\r".encode("utf-8")

BT_INQ = "AT+BTINQ?\r".encode("utf-8")

BT_MODE = ["AT+BTMODE,0\r".encode("utf-8"),
           "AT+BTMODE,1\r".encode("utf-8"),
           "AT+BTMODE,2\r".encode("utf-8"),
           "AT+BTMODE,3\r".encode("utf-8")]

BT_CANCEL = "AT+BTCANCEL\r".encode("utf-8")

ATS_S4 = "ATS4=0\r".encode("utf-8") # Gets the BT addr and leaves dev name

ATS_S24 = f"ATS24={Config.scan_amount}\r".encode("utf-8") # Change in conf.Config.scan_amount for amount of addrs to collect

ATS_S33 = "ATS33=15\r".encode("utf-8") # Change scan time to documented AddInsight time
