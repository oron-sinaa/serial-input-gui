"""sendMessage("Acc X : %.3f\n\r", xDataG);"""

import serial.tools.list_ports


def com_ports():
    # 'com_list' is a list of all available com ports
    ports = serial.tools.list_ports.comports()
    com_list = []
    for p in ports:
        com_list.append(p.device)
    return com_list


def baud_rate():
    # 'baud_list' is a list of standard baud rates
    baud_list = [4800, 9600, 19200, 38400, 57600, 115200]
    return baud_list
