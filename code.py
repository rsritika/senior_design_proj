import board
import digitalio
import time
import microcontroller

# Pressure Sensor
import adafruit_mprls
i2c = board.I2C()
mpr = adafruit_mprls.MPRLS(i2c, psi_min=0, psi_max=50)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

motor = digitalio.DigitalInOut(board.D12)
motor.direction = digitalio.Direction.OUTPUT

solenoid = digitalio.DigitalInOut(board.D10)
solenoid.direction = digitalio.Direction.OUTPUT

while True:
    motor.value = True
    time.sleep(1)
    solenoid.value = True
    time.sleep(1)
# Take pressure
while True:
    print((mpr.pressure,))
    time.sleep(1)
