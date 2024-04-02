import parani

def app_main(logger):

    logger.info("SCAN: Starting app")
    
    try:
        device = parani.Parani_SD1000(logger)
    except:
        logger.critical("SCAN: Can\'t open serial port")
        exit(1)

    device.set_s_registers()

    while True:

        device.send_heartbeat_packet()

        device.flush_buffer()

        device.bt_cancel()

        device.bt_inq_readline()
    
        device.send_imp_packets()
