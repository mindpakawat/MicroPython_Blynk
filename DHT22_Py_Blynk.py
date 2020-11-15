import network
import utime as time
from machine import Pin
import dht
import BlynkLib


WIFI_SSID = 'yourWifiID'
WIFI_PASS = 'yourPassword'
BLYNK_AUTH = 'yourAuth'
GPIO_DHT22_PIN = 4

print("Connecting to WiFi network '{}'".format(WIFI_SSID))
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
    print('WiFi connect retry ...')
print('WiFi IP:', wifi.ifconfig()[0])

print("Connecting to Blynk server...")
blynk = BlynkLib.Blynk(BLYNK_AUTH)


T_VPIN = 3
H_VPIN = 4

dht22 = dht.DHT22(machine.Pin(GPIO_DHT22_PIN))


while True:

    try:
        time.sleep(2)
        dht22.measure()
        temp = dht22.temperature()
        humi = dht22.humidity()
        blynk.virtual_write(T_VPIN, temp)
        blynk.virtual_write(H_VPIN, humi)
        print('Temperature: %3.1f C' %temp)
        print('Humidity: %3.1f %%' %humi)
    except OSError as o_err:
        print("Unable to get DHT22 sensor data: '{}'".format(o_err))



while True:
    blynk.run()






