import os
import sys
import esp

esp.osdebug(esp.LOG_DEBUG)

import gc
gc.collect()

import network

AP = True

if AP:
    station = network.WLAN(network.AP_IF)
    mac = station.config('mac')
    ssid = 'ESP32_{0}'.format(mac.hex()) # Change this if you are working in a classroom
    password = ''
    station.active(True)
    station.config(essid=ssid, password=password)
    print('connecting in AP mode...')
    while not station.active():
        pass
    print('Connection successful')
    print(station.ifconfig())

else:   

    MY_SSID = 'enter your ssid' 
    MY_PW = 'enter your password'

    station = network.WLAN(network.STA_IF)
    station.active(True)

    if not station.isconnected():
        station.connect(MY_SSID, MY_PW)

    print('connecting to :',MY_SSID)

    while station.isconnected() == False:
        pass

    print('Connection successful')
    print(station.ifconfig())

# import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
# logger.info(str(station.ifconfig()))
