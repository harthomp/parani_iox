import log
import scan

class Config:
    logging_type = "file" # file || syslog
    syslog_ipaddr = "192.168.1.3"

if __name__ == "__main__":
    
    config = Config()

    if config.logging_type == "file":
        logger = log.file_system_logger()
    elif config.logging_type == "syslog":
        print("TODO SYSLOG")
    else:
        exit()

    scan.app_main(logger)
