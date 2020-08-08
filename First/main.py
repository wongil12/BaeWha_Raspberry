import RPi.GPIO as GPIO
import csv
import time
import motor.motor as motor
import buzzer.buzzer as buzzer
import board
import adafruit_dht

pins = {}       # Save as All sensor information

# Get Pins Information
f = open('pin.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
  pins[line[0]] = [int(line[1]), line[2]]
f.close()

# Setting GPIO Mode
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Setting GPIO In, Out
for k, v in pins.items():
    if v[1] == "OUT" :
        GPIO.setup(int(v[0]), GPIO.OUT)
    elif v[1] == "IN" :
        GPIO.setup(int(v[0]), GPIO.IN)

# Setting Variables
motorPWM = GPIO.PWM(pins['motor'][0], 50)
buzzerPWM = GPIO.PWM(pins['buzzer'][0], 100)
motorPWM.start(0)

openFlag = False

openTime = 0

outDht = adafruit_dht.DHT11(board.D4)
closeTime = 0

# timezone setting
dhtStartTime = time.time()

# Check Sensor(Open, Close)
try:
    pulse_start = 0
    pulse_end = 0
    deep_start = 0
    deep_end = 0
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
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        # set Open Flag
        if distance <= 20:
            openFlag = True
            openTime = time.time()

        elif distance > 20:
            closeTime = time.time()
            # Keep Open for 5 sec
            if closeTime - openTime >= 3:
                openFlag = False
            else:
                openFlag = True
        #check Deep
        GPIO.output(pins['deepTrig'][0], False)
        time.sleep(0.5)
        
        GPIO.output(pins['deepTrig'][0], True)
        time.sleep(0.00001)
        GPIO.output(pins['deepTrig'][0], False)
        
        while GPIO.input(pins['deepEcho'][0]) == 0:
            deep_start = time.time()
        
        while GPIO.input(pins['deepEcho'][0]) == 1:
            deep_end = time.time()
        
        deep_duration = deep_end - deep_start
        deep_distance = deep_duration * 17000
        deep_distance = round(deep_distance, 2)
        # Motor Open
        if openFlag == True:
            motor.Open(motorPWM)
        # Motor Close
        elif openFlag == False:
            motor.Close(motorPWM)
        # Get Temperature And Get Humidity
        if dhtStartTime + 60 < time.time() :
            dhtStartTime = time.time()
            temp = outDht.temperature
            hum = outDht.humidity
            print("outTemp: "+str(temp)+" outTemp: "+str(hum))
        if GPIO.input(pins['fire'][0]) == 0:
            buzzer.melody(buzzerPWM)
            print("Fire!!!!!")
except KeyboardInterrupt:
    motorPWM.stop()
GPIO.cleanup()