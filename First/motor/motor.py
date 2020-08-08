# Open Module
def Open(pwm):
    pwm.ChangeDutyCycle(9)

# Close Module
def Close(pwm):
    pwm.ChangeDutyCycle(3.5)