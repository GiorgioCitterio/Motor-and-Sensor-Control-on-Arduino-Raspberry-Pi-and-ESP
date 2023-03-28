import paho.mqtt.publish as publish
import time
TOPIC = "ciao"
BROKER = "test.mosquitto.org"

i = 0
while True:
    i += 1
    msg=str(i)
    print(msg)

    publish.single(TOPIC, msg, hostname=BROKER)

    time.sleep(5)