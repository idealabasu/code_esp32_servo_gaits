
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

redirect_template = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" http-equiv="refresh" content=".5; url='/'" />
  </head>
  <body>
    <p>Success</p>
  </body>
</html>'''


import uasyncio
from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template

# setup webserver
app = Microdot()

Response.default_content_type = 'text/html'
Response.socket_read_timeout =0

@app.route('/')
async def index(request):
    html = template.format(led_value= led.value(),frequency=time_based_servo.f, amplitude=time_based_servo.A, offset = time_based_servo.b, l0=time_based_servo.l1, l1 = time_based_servo.l2, l2 = time_based_servo.l3, l3 = time_based_servo.l4)
    return html#, 200, {'Content-Type': 'text/html'}


from machine import Pin
import time_based_servo

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
    # html = redirect_template
    html = template.format(led_value= led.value(),frequency=time_based_servo.f, amplitude=time_based_servo.A, offset = time_based_servo.b, l0=time_based_servo.l1, l1 = time_based_servo.l2, l2 = time_based_servo.l3, l3 = time_based_servo.l4)
    return html#, 202, {'Content-Type': 'text/html'}

def start_server():
    print('Starting microdot app')
    try:
        app.run(port=80)
    except:
        app.shutdown()

# start_server()