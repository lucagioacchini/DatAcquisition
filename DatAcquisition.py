#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This is the Main of the DatAcquisition program. 
DatAcquisition v.0.2.0

2018 Luca Gioacchini
"""

#from docs.user_interface import Gui
from docs.layout import Layout

from Tkinter import*
import docs.src.functions as sensor

root = Tk()
root.iconbitmap('docs\img\icon.ico')
my_gui = Layout(root)
sensor.start_sensor()
root.mainloop()
