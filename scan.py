import parani
import os
import logging
import time

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

    while True:
        x.flush_buffer()
        
        logger.info("Flush occurred")

        x.bt_cancel()

        print(x.response)
        
        logger.info("bt_cancel: " + str(x.response))

        x.bt_inq()
    
        i = x.response
    
        logger.info("bt_inq: " + str(x.response))

        print(i)
        
        time.sleep(3)

        
        # PARSER NOT NEEDED RIGHT NOW.
        #i = i.split(b"\r\n")

        #scan_list = []

        #for x in i:
        #    if not x == b"":
        #        scan_list.append(x)
    
        #for record in scan_list:
        #    print(record)

