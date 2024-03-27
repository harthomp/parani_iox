import parani

def app_main(logger):

    logger.info('Starting app')
    
    try:
        device = parani.Parani_SD1000()
    except:
        logger.info('Can\'t open serial port')
        exit(1)

    device.set_s_registers()

    logger.info("Set S registers")

    while True:

        # Heartbeat packet
        device.send_heartbeat_packet()

        device.flush_buffer()
        
        logger.info("Flush occurred")

        device.bt_cancel()
 
        logger.info("BTCANCEL: " + str(device.response))

        device.bt_inq_readline()
    
        device.send_imp_packets()
