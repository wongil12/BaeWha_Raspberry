import time

scale = [261, 294, 329, 349, 392, 440, 493]

list = [0,0,4,4,5,5,4,3,3,2,2,1,1,0]
def melody(pwm):
    for i in range(len(list)):
        pwm.ChangeFrequency(scale[list[i]])
        if (i+1)%7 == 0:
            time.sleep(1)
        else:
            time.sleep(0.5)