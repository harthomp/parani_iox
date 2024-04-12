class Config:
    logging_type = "file" # file || syslog
    syslog_server_ipaddr = "192.168.1.3"

    # Transmission information
    addinsight_server_ipaddr = "192.168.1.2"
    addinsight_server_port = 2000
        
    scan_amount = "30" # Used in payloads for num of addr collected during INQ

