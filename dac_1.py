import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
GPIO.setup(dac, GPIO.OUT)

def binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

# v = int(input())

# if 0 <= v <= 256:
#     voltage = (3.3/2**8) * v
#     print(voltage)
#     bin = binary(v)
#     print(bin)
#     GPIO.output(dac, bin)
try:
    while True:
        v = int(input())
        if 0 <= v <= 256:
            voltage = (3.3/2**8) * v
            print(voltage)
            binn = binary(v)
            print(binn)
            GPIO.output(dac, binn)
finally:
    GPIO.setup(dac,0)