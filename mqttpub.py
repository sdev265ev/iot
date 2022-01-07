import paho.mqtt.client as mqtt #import the client
def Pubmqtt(topic, message, qos=0, retain=True):
	brokerAddress="192.168.254.55"
	#brokerAddress="test.mosquitto.org"
	port=1883
	client = mqtt.Client()
	client.username_pw_set("mqttuser", "mqttpass")
	client.connect(brokerAddress, port)
	client.publish(topic, message, qos, retain)
	client1.disconnect()
