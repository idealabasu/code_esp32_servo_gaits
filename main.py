
import uasyncio as asyncio
import microdot_api
import time_based_servo



# async def runme():
#     ii = 0
#     while True:
#         print(ii)
#         ii+=1
#         await asyncio.sleep(0.5)

servo_task = asyncio.create_task(time_based_servo.update_servo_loop())

microdot_api.start_server()

# print('something else happens')

# # here is our main loop
# while True:
#     time_based_servo.update_servos()