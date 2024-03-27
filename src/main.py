import log
import scan

class Config:
    logging_type = "file" # file || syslog
    syslog_server_ipaddr = "192.168.1.3"
    scan_amount = "30" # Used in payloads for num of addr collected during INQ

if __name__ == "__main__":
    
    if Config.logging_type == "file":
        logger = log.file_system_logger()
    elif Config.logging_type == "syslog":
        print("TODO SYSLOG")
    else:
        exit()

    scan.app_main(logger)
