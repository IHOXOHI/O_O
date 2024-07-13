import pyb
import machine
from time import ticks_ms, sleep_ms
##BE CAREFULL!!! There is ONLY SCREEN to open a stream with the board, which works.

sw = pyb.Switch()

t1 = ticks_ms()
t2 = ticks_ms()
n = 0

while (t2 - t1) < 5000:
    pyb.LED(3).on()
    t2 = ticks_ms()
    if sw.value():
        n += 1
    sleep_ms(500)
pyb.LED(3).off()
if n == 2:
    pyb.usb_mode('VCP')
else:
    while n < 100:
        for i in range(250):
            i += 1
            pyb.LED(4).intensity(i)
            sleep_ms(10)##**
        for i in range(250):
            j = 251 - i
            pyb.LED(4).intensity(j)
            sleep_ms(10)##**
        ##**maybe your board doesn't have enought speed to do it, ..., so to adapt to each board... The best security is the faster!