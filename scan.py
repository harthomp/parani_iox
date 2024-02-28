import parani

if __name__ == "__main__":
    
    x = parani.Parani_SD1000()

    x.bt_cancel()

    print(x.response)

    x.bt_inq()

    i = x.response

    print(i)

    i = i.split(b"\r\n")

    scan_list = []

    for x in i:
        if not x == b"":
            scan_list.append(x)
    
    for record in scan_list:
        print(record)

