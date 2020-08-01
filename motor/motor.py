# Open Module
def Open(pwm):
    pwm.ChangeDutyCycle(12)
    print("Open")

# Close Module
def Close(pwm):
    pwm.ChangeDutyCycle(3)
    print("Close")