import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
        print("message received " ,str(message.payload.decode("utf-8")))
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)
########################################
broker_address="192.168.254.55"
#broker_address="test.mosquitto.org"
print("creating new instance")
client = mqtt.Client() #create new instance
client.username_pw_set("mqttuser", "mqttpass")
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","test/status")
client.subscribe("test/status")

for x in range(20):
        #print("Publishing message to topic","test/status")
        #client.publish("test/status", "Hello World")
        #client.publish("test/status","on")

        time.sleep(4) # wait
#client.loop_stop() #stop the loop


