import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)

def binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
t = int(input())
T = t/1020
try:
    while True:
        v = int(0)
        if v == 0:
            while v != 255:
                voltage = (3.3/2**8) * v
                print(voltage)
                binn = binary(v)
                print(binn)
                GPIO.output(dac, binn)
                time.sleep(T)
                v+=1

        if v == 255:
            while v != 0:
                voltage = (3.3/2**8) * v
                print(voltage)
                binn = binary(v)
                print(binn)
                GPIO.output(dac, binn)
                time.sleep(T)
                v-=1
finally:
    GPIO.setup(dac,0)
