from datetime import datetime
import time
import paho.mqtt.publish as publish

while True:
    with open('1mb', "br") as f:
        publish.single("paho/test/single", f.read(), hostname="192.168.2.109")
    time.sleep(0.2)