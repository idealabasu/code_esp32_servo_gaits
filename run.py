# import logging
# logger = logging.getLogger(__name__)
import gc
import uasyncio as asyncio
import time_based_servo
# Complete project details at https://RandomNerdTutorials.com
# https://randomnerdtutorials.com/micropython-ssd1306-oled-scroll-shapes-esp32-esp8266/
# https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/

import sys
sys.path.insert(0,'/code/lib')


import time

import micropython

# logger.info(str(micropython.mem_info()))


# logger.info(str(micropython.mem_info()))
print(micropython.mem_info())
gc.collect()
# logger.info(str(micropython.mem_info()))
print(micropython.mem_info())

import microdot
import microdot.microdot
import microdot.utemplate
import microdot.websocket
# from microdot.microdot import Microdot, Response, send_file

import time_based_servo



app = microdot.microdot.Microdot()

microdot.microdot.Response.default_content_type = 'text/html'
microdot.microdot.Response.socket_read_timeout =0

# @app.route('/')
# async def index(request):
#     html = template.format(led_value= led.value(),frequency=time_based_servo.f, amplitude=time_based_servo.A, offset = time_based_servo.b, l0=time_based_servo.l1, l1 = time_based_servo.l2, l2 = time_based_servo.l3, l3 = time_based_servo.l4)
#     return html

# root route
# @app.route('/')
# async def index(request):
#     return microdot.utemplate.Template('index.html').render()

class ServoParams(object):
    def __init__(self,f=1,a=180,b=0,l=0):
        self.f = f
        self.a = a
        self.b = b
        self.l = l

    def get_params(self):
        d = {}
        d['a'] = self.a
        d['b'] = self.b
        d['f'] = self.f
        d['l'] = self.l
        return d

    def set_params(self,dictionary1):
        self.a = dictionary1['a']
        self.b = dictionary1['b']
        self.f = dictionary1['f']
        self.l = dictionary1['l']


servo1_params = ServoParams()

import json

import random

async def run_imu():
    data = {}
    data['temp'] = random.randint(0,0b1111111111)
    data['gyro'] = random.randint(0,0b1111111111)
    data['accel'] = random.randint(0,0b1111111111)
    return data

@app.route('/ws')
@microdot.websocket.with_websocket
async def read_form(request, ws):
    while True:
        try:
            data = await ws.receive()
            await ws.send(data)
            json_data = json.loads(data)
            time_based_servo.A  = float(json_data['amplitude'])
            time_based_servo.f  = float(json_data['frequency'])
            print(data)
        except Exception as e:
            print(e)

@app.route('/sensordata')
@microdot.websocket.with_websocket
async def sensordata(request, ws):
    while True:
        data = await run_imu()
        # data = all_data[50]
        await ws.send(json.dumps(data))
        await asyncio.sleep(.5)

# Static CSS/JSS
@app.route("/static/<path:path>")
def static(request, path):
    if ".." in path:
        # directory traversal is not allowed
        return "Not found", 404
    return microdot.microdot.send_file("static/" + path)


# shutdown
@app.get('/shutdown')
def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'



# def set_servo(value):
#     led.value(int(value))

#     print('setting servo value: ',value)

# def set_frequency(value):
#     time_based_servo.f = float(value)
#     print('setting f: ',value)

# def set_amplitude(value):
#     time_based_servo.A = float(value)
#     print('setting f: ',value)

# def set_offset(value):
#     time_based_servo.b = float(value)
#     print('setting f: ',value)

# def set_l0(value):
#     time_based_servo.l1 = float(value)
#     print('setting f: ',value)

# def set_l1(value):
#     time_based_servo.l2 = float(value)
#     print('setting f: ',value)

# def set_l2(value):
#     time_based_servo.l3 = float(value)
#     print('setting f: ',value)

# def set_l3(value):
#     time_based_servo.l4 = float(value)
#     print('setting f: ',value)


@app.get('/')
async def index(request):
    try:
        pass
        # set_servo((int(request.args['servoval'])))
        # set_frequency((request.args['frequency']))
        # set_amplitude((request.args['amplitude']))
        # set_offset((request.args['offset']))
        # set_l0((request.args['l0']))
        # set_l1((request.args['l1']))
        # set_l2((request.args['l2']))
        # set_l3((request.args['l3']))
    except KeyError:
        pass
        # set_servo(0)
        # set_frequency(1)
        # set_amplitude(90)
        # set_offset(90)
        # set_l0(0)
        # set_l1(.25)
        # set_l2(.5)
        # set_l3(.75)
    # html = template.format(led_value= led.value(),frequency=time_based_servo.f, amplitude=time_based_servo.A, offset = time_based_servo.b, l0=time_based_servo.l1, l1 = time_based_servo.l2, l2 = time_based_servo.l3, l3 = time_based_servo.l4)
    return microdot.utemplate.Template('index2.html').render()

def start_server():
    print('Starting microdot app')
    try:
        app.run(port=5000)
    except:
        app.shutdown()

# logger.info('getting down to servo task')

async def update_servo_loop():
    ii = 0
    while True:
        # print(ii)
        ii+=1
        time_based_servo.update_servos()
        await asyncio.sleep(0.01)

servo_task = asyncio.create_task(update_servo_loop())
    
all_data = []

async def get_imu():
    global all_data
    ii = 0
    while True:
        data = await run_imu()
        all_data.append(data)
        while len(all_data)>50:
            all_data.pop(0)
        await asyncio.sleep(0.1)


start_server()


