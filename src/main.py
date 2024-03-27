from conf import Config
import log
import scan

if __name__ == "__main__":
    
    if Config.logging_type == "file":
        logger = log.file_system_logger()
        logger.info("INIT FS LOGGER")
    elif Config.logging_type == "syslog":
        logger = log.syslog_logger()
        logger.info("INIT SYSLOG LOGGER")
    else:
        exit()

    scan.app_main(logger)
