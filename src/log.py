import os
import logging
from logging.handlers import SysLogHandler
from conf import Config

def file_system_logger():    
    log_file_dir = "/tmp"
    log_file_path = os.path.join(log_file_dir, "iox-serial-port.log")

    logging.basicConfig(
        filename = log_file_path,
        level = logging.INFO,
        format = '[%(asctime)s]{%(pathname)s:%(lineno)d}%(levelname)s- %(message)s',
        datefmt = '%H:%M:%S'
            )

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)

    logging.getLogger('').addHandler(console)
    logger = logging.getLogger(__name__)
    
    return logger

def syslog_logger():
    logging.basicConfig(
        level = logging.INFO,
        format = '[%(asctime)s]{%(pathname)s:%(lineno)d}%(levelname)s- %(message)s',
        datefmt = '%H:%M:%S'
            )
    
    console = SysLogHandler(address = (Config.syslog_server_ipaddr, 514))
    console.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)

    logging.getLogger('').addHandler(console)
    logger = logging.getLogger(__name__)
    
    return logger