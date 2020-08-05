# Open Module
def Open(pwm):
    pwm.ChangeDutyCycle(9)
    print("Open")

# Close Module
def Close(pwm):
    pwm.ChangeDutyCycle(3.5)
    print("Close")