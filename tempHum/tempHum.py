import board
import adafruit_dht

def getDht(dht) :
    temp = dht.temperature
    hum = dht.humidity
    return temp, hum
    