
import uasyncio as asyncio
import time_based_servo
# Complete project details at https://RandomNerdTutorials.com
# https://randomnerdtutorials.com/micropython-ssd1306-oled-scroll-shapes-esp32-esp8266/
# https://randomnerdtutorials.com/micropython-oled-display-esp32-esp8266/


from machine import Pin, SoftI2C
import machine
import time
import bno055
import bno055.bno055

import microdot
import microdot.microdot
import microdot.utemplate
import microdot.websocket
# from microdot.microdot import Microdot, Response, send_file

from machine import Pin
import time_based_servo


# from microdot import Microdot, Response, send_file
# from microdot.utemplate import Template
# from microdot.websocket import with_websocket
# from ldr_photoresistor_module import LDR
# import time


template = '''
<!DOCTYPE html>
<html>
  <head>
    <title>URL Encoded Forms</title>
  </head>
  <body>
    <form
      action="/test"
      method="GET"
      enctype="application/x-www-form-urlencoded">
      <p>LED:<input type="text" name="servoval" value="{led_value}" /></p>
      <p>Frequency:<input type="text" name="frequency" value="{frequency}" /></p>
      <p>Amplitude:<input type="text" name="amplitude" value="{amplitude}" /></p>
      <p>Offset:<input type="text" name="offset" value="{offset}" /></p>
      <p>L0:<input type="text" name="l0" value="{l0}" /></p>
      <p>L1:<input type="text" name="l1" value="{l1}" /></p>
      <p>L2:<input type="text" name="l2" value="{l2}" /></p>
      <p>L3:<input type="text" name="l3" value="{l3}" /></p>
      <p><input type="submit" value="Submit" /><p>
    </form>
  </body>
</html>
'''


app = microdot.microdot.Microdot()

microdot.microdot.Response.default_content_type = 'text/html'
microdot.microdot.Response.socket_read_timeout =0

@app.route('/')
async def index(request):
    html = template.format(led_value= led.value(),frequency=time_based_servo.f, amplitude=time_based_servo.A, offset = time_based_servo.b, l0=time_based_servo.l1, l1 = time_based_servo.l2, l2 = time_based_servo.l3, l3 = time_based_servo.l4)
    return html

# app = microdot.microdot.Microdot()

# microdot.microdot.Response.default_content_type = 'text/html'

# # root route
# @app.route('/')
# async def index(request):
#     return Template('index.html').render()



# @app.route('/ws')
# @microdot.websocket.with_websocket
# async def read_sensor(request, ws):
#     while True:
# #         data = await ws.receive()
#         time.sleep(.1)
#         try:
#             await ws.send(str(ldr.get_light_percentage()))
#         except ConnectionResetError:
#             print("connection lost")

# # Static CSS/JSS
# @app.route("/static/<path:path>")
# def static(request, path):
#     if ".." in path:
#         # directory traversal is not allowed
#         return "Not found", 404
#     return send_file("static/" + path)


# # shutdown
# @app.get('/shutdown')
# def shutdown(request):
#     request.app.shutdown()
#     return 'The server is shutting down...'


led = Pin(2, Pin.OUT)

def set_servo(value):
    led.value(int(value))

    print('setting servo value: ',value)

def set_frequency(value):
    time_based_servo.f = float(value)
    print('setting f: ',value)

def set_amplitude(value):
    time_based_servo.A = float(value)
    print('setting f: ',value)

def set_offset(value):
    time_based_servo.b = float(value)
    print('setting f: ',value)

def set_l0(value):
    time_based_servo.l1 = float(value)
    print('setting f: ',value)

def set_l1(value):
    time_based_servo.l2 = float(value)
    print('setting f: ',value)

def set_l2(value):
    time_based_servo.l3 = float(value)
    print('setting f: ',value)

def set_l3(value):
    time_based_servo.l4 = float(value)
    print('setting f: ',value)


@app.get('/test')
async def servo(request):
    set_servo((int(request.args['servoval'])))
    set_frequency((request.args['frequency']))
    set_amplitude((request.args['amplitude']))
    set_offset((request.args['offset']))
    set_l0((request.args['l0']))
    set_l1((request.args['l1']))
    set_l2((request.args['l2']))
    set_l3((request.args['l3']))
    html = template.format(led_value= led.value(),frequency=time_based_servo.f, amplitude=time_based_servo.A, offset = time_based_servo.b, l0=time_based_servo.l1, l1 = time_based_servo.l2, l2 = time_based_servo.l3, l3 = time_based_servo.l4)
    return html

def start_server():
    print('Starting microdot app')
    try:
        app.run(port=80)
    except:
        app.shutdown()


servo_task = asyncio.create_task(time_based_servo.update_servo_loop())

# i2c = SoftI2C(scl=Pin(33), sda=Pin(32))

# imu = bno055.bno055.BNO055(i2c)

# async def read_imu():
#     calibrated = False
#     while True:
#         if not calibrated:
#             calibrated = imu.calibrated()
#             print('Calibration required: sys {} gyro {} accel {} mag {}'.format(*imu.cal_status()))
#         print('Temperature {}°C'.format(imu.temperature()))
#         print('Mag       x {:5.0f}    y {:5.0f}     z {:5.0f}'.format(*imu.mag()))
#         print('Gyro      x {:5.0f}    y {:5.0f}     z {:5.0f}'.format(*imu.gyro()))
#         print('Accel     x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.accel()))
#         print('Lin acc.  x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.lin_acc()))
#         print('Gravity   x {:5.1f}    y {:5.1f}     z {:5.1f}'.format(*imu.gravity()))
#         print('Heading     {:4.0f} roll {:4.0f} pitch {:4.0f}'.format(*imu.euler()))
#         await asyncio.sleep(0.1)

# imu_task = asyncio.create_task(read_imu())

start_server()


