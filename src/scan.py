import parani
import transmission
from datetime import datetime, timezone

def app_main(logger):

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
        x.send_heartbeat_packet()

        x.flush_buffer()
        
        logger.info("Flush occurred")

        x.bt_cancel()

        print(x.response)
        
        logger.info("BTCANCEL: " + str(x.response))

        x.bt_inq_readline()
    
        x.send_imp_packets()
