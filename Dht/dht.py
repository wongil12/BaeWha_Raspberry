import board
import adafruit_dht


def getTmp(dht) :
    tmp = dht.temperature
def getHum(dht) :
    hum = dht.humidity

def getDht() :
    inDht = adafruit_dht.DHT11(board.D4)
    outDht = adafruit_dht.DHT11(board.D21)
    return getTmp(inDht), getHum(inDht), getTmp(outDht), getHum(outDht)
    