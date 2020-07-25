import RPi.GPIO as GPIO
import motor.motor as motor
import csv

pins = {}       # Save as All sensor information

# Get Pins Information
f = open('pin.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
  pins[line[0]] = [int(line[1]), line[2]]
f.close()

# Setting GPIO Mode
GPIO.setmode(GPIO.BCM)

# Setting GPIO In, Out
for k, v in pins.items():
    if v[1] == "OUT" :
        GPIO.setup(int(v[0]), GPIO.OUT)
    elif v[1] == "IN"
        GPIO.setup(int(v[0]), GPIO.IN)

# Setting Variables
motorPWM = GPIO.PWM(pins['motor'][0], 50)
motorPWM.start(0)

# Check Sensor(Open, Close)
try:
    while True:
        GPIO.output(pins['openTrig'][0], False)
        time.sleep(0.5)
        
        GPIO.output(pins['openTrig'][0], True)
        time.sleep(0.00001)
        GPIO.output(pins['openTrig'][0], False)
        
        while GPIO.input(pins['openEcho'][0]) == 0:
            pulse_start = time.time()
        
        while GPIO.input(pins['openEcho'][0]) == 1:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        distance = pulse_start * 17000
        distance = round(distance, 2)

        # Open
        if distance <= 100:
            motor.Open(motorPWM)
        # Close
        elif distance > 100:
            motor.Close(motorPWM)
except KeyboardInterrupt:
    motorPWM.stop()
GPIO.cleanup()