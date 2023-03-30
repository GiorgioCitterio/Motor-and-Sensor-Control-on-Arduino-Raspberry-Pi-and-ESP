import paho.mqtt.client as client
TOPIC="umbeGio2"
BROKER = "172.17.4.29"

def on_connect(subscriber, userdata, flags, rc):
    print("Connesso con return code" + str(rc))

    subscriber.subscribe(TOPIC)

def on_message(subscriber, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

subscriber = client.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message

subscriber.connect(BROKER, 1883, 60)

subscriber.loop_forever()