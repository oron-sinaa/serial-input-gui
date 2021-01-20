"""sendMessage("Acc X : %.3f\n\r", xDataG);"""

import serial
from tkinter import *


def com_port():
    com_num = 'COM' + int(input())
    return com_num


def baud_rate():
    baud_rate = int(input())
    return baud_rate


def confirm():
    print('Established serial connection at',
          com_port(), 'at', baud_rate(), 'baud rate')


controller = serial.Serial(com_port(), baud_rate())

list_values = []
list_in_floats = []

data = controller.read()
decoded_values = str(data[0:len(data)].decode("utf-8"))
list_values = decoded_values.split(',')

for item in list_values:
    list_in_floats.append(float(item))
