# main.py -- put your code here!
#import time_based_servo
#import wifi_based_control_form

import os
import sys
import esp
from secrets import *

esp.osdebug(esp.LOG_DEBUG)

import gc
gc.collect()

import network

AP = True

if AP:
    ssid = 'SCRAM'
    password = ''
    station = network.WLAN(network.AP_IF)
    station.active(True)
    station.config(essid=ssid, password=password)
    print('connecting in AP mode...')
    while not station.active():
        pass
    print('Connection successful')
    print(station.ifconfig())
else:   
    ssid = MY_SSID
    password = MY_PW
    station = network.WLAN(network.STA_IF)
    station.active(True)

    if not station.isconnected():
        station.connect(ssid, password)

    print('connecting to :',ssid)
    while station.isconnected() == False:
        pass

    print('Connection successful')
    print(station.ifconfig())


try:
    os.rename('lib/microdot.py','lib/microdot.py')
except:
              

    import mip

    mip.install('https://github.com/miguelgrinberg/microdot/raw/main/src/microdot.py')
    # mip.install('https://github.com/miguelgrinberg/microdot/raw/main/src/microdot_asyncio.py')
    mip.install('https://github.com/miguelgrinberg/microdot/raw/main/src/microdot_utemplate.py')


    # del mip
    # del uos
    # gc.collect()

    mip.install('https://github.com/miguelgrinberg/microdot/raw/main/libs/common/utemplate/source.py')
    mip.install('https://github.com/miguelgrinberg/microdot/raw/main/libs/common/utemplate/recompile.py')
    mip.install('https://github.com/miguelgrinberg/microdot/raw/main/libs/common/utemplate/compiled.py')
    try:
        os.mkdir('lib/utemplate')
    except OSError:
        pass
    os.rename('lib/source.py','lib/utemplate/source.py')
    os.rename('lib/recompile.py','lib/utemplate/recompile.py')
    os.rename('lib/compiled.py','lib/utemplate/compiled.py')

    #soft reboot
    sys.exit()
