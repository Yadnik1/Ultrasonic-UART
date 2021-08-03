from machine import UART,Pin
import time,utime
import sys


class US100:

    def __init__(self,uart):
        self.uart = uart

    def distance_mm(self):
            
            utime.sleep_ms(1)
            uart.write(b'\x55')
            t = 0
            buf = bytearray(2)
            while t < 1000:
                t = t + 1
                utime.sleep_ms(500)
            if t < 1000:
                uart.readinto(buf, 2)           
            dist = buf[0] * 256 + buf[1]
            if dist > 1100:
                    dist = -1
            return dist


uart=UART("UART_0")
sonar=US100(uart)
while True:
    obstacle_distance=sonar.distance_mm()
    print(obstacle_distance)

    
