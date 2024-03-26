import log
import scan

if __name__ == "__main__":
    logger = log.file_system_logger()
    scan.app_main(logger)
