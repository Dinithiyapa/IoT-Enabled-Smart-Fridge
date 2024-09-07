import time 
from umqttsimple import MQTTClient 
import ubinascii 
import machine 
import micropython 
import network 
import esp 
from machine import Pin 
import dht 
esp.osdebug(None) 
import gc 
gc.collect() 
import urequests as requests 

ssid = 'Exam' 
password = 'Exam@2023' 
mqtt_server = '13.51.201.221'  # Replace with your MQTT Broker IP 

THINGSPEAK_API_KEY = "JV9AZ3COKIXTQ0FJ" 
THINGSPEAK_URL1 = "https://api.thingspeak.com/update?api_key=JV9AZ3COKIXTQ0FJ&field1=0" 

client_id = ubinascii.hexlify(machine.unique_id()) 

TOPIC_PUB_TEMP = b'esp/dht/temperature' 
TOPIC_PUB_HUM = b'esp/dht/humidity' 
TOPIC_PUB_DIS = b'esp/dht/distance' 
TOPIC_PUB_NOT = b'esp/dht/notification' 
TOPIC_PUB_DNOT = b'esp/dht/dnotifi' 

last_message = 0 
message_interval = 5 

sensor = dht.DHT22(Pin(16)) 

station = network.WLAN(network.STA_IF) 
station.active(True) 
station.connect(ssid, password) 

while station.isconnected() == False: 
    pass 

print('Connection successful') 
print(station.ifconfig()) 

def send_temp(data): 
    response = requests.get(THINGSPEAK_URL1 + "&field1=" + str(data))
