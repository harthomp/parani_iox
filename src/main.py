from conf import Config
import log
import scan

if __name__ == "__main__":
    
    if Config.logging_type == "file":
        logger = log.file_system_logger()
    elif Config.logging_type == "syslog":
        logger = log.syslog_logger()
    else:
        exit()

    scan.app_main(logger)
