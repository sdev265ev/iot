import paho.mqtt.client as mqtt #import the client1
def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
	print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
	client.subscribe("digitest/test1")  # Subscribe to the topic “digitest/test1”, receive any messages published on it

def GetMessage(topic):
	broker_address="192.168.254.55"
	#broker_address="test.mosquitto.org"
	client = mqtt.Client("test")  # Create instance of client with client ID “digi_mqtt_test”
	client.on_connect = on_connect  # Define callback function for successful connection
	# client.connect("m2m.eclipse.org", 1883, 60)  # Connect to (broker, port, keepalive-time)
	client.connect(broker, 17300)
	
