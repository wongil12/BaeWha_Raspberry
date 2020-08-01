import board
import adafruit_dht


def getTmp(dht) :
    tmp = dht.temperature
    return tmp
def getHum(dht) :
    hum = dht.humidity
    return hum
def getDht() :
    inDht = adafruit_dht.DHT11(board.D4)
    outDht = adafruit_dht.DHT11(board.D21)
    return getTmp(inDht), getHum(inDht), getTmp(outDht), getHum(outDht)
    