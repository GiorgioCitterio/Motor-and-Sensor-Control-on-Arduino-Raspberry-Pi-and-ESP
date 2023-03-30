import paho.mqtt.publish as publish
import time
TOPIC = "umbeGio2"
BROKER = "172.17.4.29"

i = 0
while True:
    i += 1
    msg=str(i)
    print(msg)

    publish.single(TOPIC, msg, hostname=BROKER)

    time.sleep(5)