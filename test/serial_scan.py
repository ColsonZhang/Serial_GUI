import serial.tools.list_ports

def Get_Used_Com():
    used_com = []
    port_list = list(serial.tools.list_ports.comports())
    if( len(port_list) > 0 ):
        for p in port_list:
            used_com.append({"device":p.device, "name":p.name, "description":p.description })
    return used_com


if __name__ == '__main__':
    scan = Get_Used_Com()
    print(scan)