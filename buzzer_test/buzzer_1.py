import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer1 = 12
buzzer2 = 18

GPIO.setup(buzzer1, GPIO.OUT)
GPIO.setup(buzzer2, GPIO.OUT)

f = GPIO.PWM(buzzer1, 100)
s = GPIO.PWM(buzzer2, 100)

try:
    f.start(100)
    s.start(100)

    f.ChangeDutyCycle(90)
    s.ChangeDutyCycle(90)

    f.ChangeFrequency(261)
    s.ChangeFrequency(329)

    f.stop()
    s.stop()
except KeyboardInterrupt:
    GPIO.cleanup()