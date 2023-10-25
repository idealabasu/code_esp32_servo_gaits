
import uasyncio as asyncio
import microdot_api
import time_based_servo

servo_task = asyncio.create_task(time_based_servo.update_servo_loop())

microdot_api.start_server()
