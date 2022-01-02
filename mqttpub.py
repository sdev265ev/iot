import paho.mqtt.client as mqtt #import the client
def Pubmqtt(topic, message):
	broker_address="192.168.254.55"
	#broker_address="test.mosquitto.org"
	client = mqtt.Client()
	client.username_pw_set("mqttuser", "mqttpass")
	client.connect(broker_address)
	client.publish(topic, message)
	client1.disconnect()
