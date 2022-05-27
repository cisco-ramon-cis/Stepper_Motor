from d1motor import Motor
from machine import I2C, Pin
from time import sleep

sda = 21 
scl = 22

i2c = I2C(1,sda=Pin(sda),scl=Pin(scl))
print(i2c.scan())
print(i2c)
a12 = Motor(0, i2c)


a12.speed(7000)
sleep(5)
a12.brake()
