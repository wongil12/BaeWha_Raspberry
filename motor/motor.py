# Open Module
def Open(pwm):
    pwm.ChangeDutyCycle(12.5)
    print("Open")

# Close Module
def Close(pwm):
    pwm.ChangeDutyCycle(7.5)
    print("Close")