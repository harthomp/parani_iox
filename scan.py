import parani
import os
import logging
import time
import transmission
from datetime import datetime, timezone

if __name__ == "__main__":
    
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

    logger.info('Starting app')
    
    try:
        x = parani.Parani_SD1000()
    except:
        logger.info('Can\'t open serial port')
        exit(1)

    x.set_s_registers()

    logger.info("Set S registers")

    while True:

        # Heartbeat packet
        x.set_packet_parameters(b"            ", datetime.now(timezone.utc))
        transmission.send_packet_v1(x.packet)

        x.flush_buffer()
        
        logger.info("Flush occurred")

        x.bt_cancel()

        print(x.response)
        
        logger.info("BTCANCEL: " + str(x.response))

        x.bt_inq_readline()
    
        if not x.response_tuples:
            logger.info("NO BT ADDRS DETECTED")
        else:
            for mac_addr, timestamp in x.response_tuples:
                logger.info("BTINQ: " + str(mac_addr) + str(timestamp))
            
                x.set_packet_parameters(mac_addr, timestamp)

                logger.info("CRAFTED PACKET")
    
                transmission.send_packet_v1(x.packet)
