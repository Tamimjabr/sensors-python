import machine
import time
import pycom
from machine import Pin
from machine import Timer


powerOn = False
pycom.heartbeat(False)

p_in = Pin('P10', mode=Pin.IN)  # SENSOR BUTTON FORM ELEKTROKIT


while(1):
    val = p_in()  # get value, 0 or 1
    if val == 0:
        if (powerOn):
            powerOn = False
            print(powerOn)
        else:
            powerOn = True
            print(powerOn)

            motionDetected = 1
            noMotionDetected = 0
            hold_time_sec = 0.1
            pir = Pin('P4', mode=Pin.IN)

            chrono = Timer.Chrono()
            chrono.start()

            print("Starting Detection")
            pycom.rgbled(0x00FF00)  # Green
            time.sleep(1)
            pycom.rgbled(0x000000)
            while True:
                if pir() == motionDetected:
                    print(chrono.read(), "Motion Detected!")
                    pybytes.send_signal(1, "Motion Detected!")
                    print("sending: Motion Detected!")
                    pycom.rgbled(0xFF0000)  # Red
                    time.sleep(10)


                if pir() == noMotionDetected:
                    pycom.rgbled(0x000000)
                    pass
                time.sleep(1)
                val2 = p_in()
                if val2 == 0:
                    powerOn = False
                    print("Stop detection")
                    pycom.rgbled(0x0000FF)  # blue
                    time.sleep(1)
                    pycom.rgbled(0x000000)
                    break
    time.sleep(1)
