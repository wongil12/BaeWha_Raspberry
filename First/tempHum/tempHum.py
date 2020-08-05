import board
import adafruit_dht

outDht = adafruit_dht.DHT11(board.D4)
inDht = adafruit_dht.DHT11(board.D21)

def getDht(dht) :
    temp = dht.temperature
    hum = dht.humidity
    return temp, hum
    
oTemp = outDht.temperature
oHum = outDht.humidity
iTemp = inDht.temperature
iHum = inDht.humidity

print(str(oTemp) + " " + str(oHum) + " " + str(iTemp) + " " + str(iHum))