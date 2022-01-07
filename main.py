#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import ADS1256
import RPi.GPIO as GPIO
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

try:
	ADC = ADS1256.ADS1256()
	ADC.ADS1256_init()
	x = 2**24
	print (x)
	ADC_Value = ADC.ADS1256_GetAll()
	print ("0 ADC = ", ADC_Value[0])
	print ("0 ADC = ", ADC_Value[0] * 5)
	print ("0 ADC = ", ADC_Value[0] * 5 / x)
	print ("0 ADC = %lf"%(ADC_Value[0]*5.0/0x7fffff))
	print ()
	print ()
	while(1):
		ADC_Value = ADC.ADS1256_GetAll()
		print ("0 ADC = %lf"%(ADC_Value[0]*5.0/0x7fffff))
		print ("1 ADC = %lf"%(ADC_Value[1]*5.0/0x7fffff))
		print ("2 ADC = %lf"%(ADC_Value[2]*5.0/0x7fffff))
		print ("3 ADC = %lf"%(ADC_Value[3]*5.0/0x7fffff))
		print ("4 ADC = %lf"%(ADC_Value[4]*5.0/0x7fffff))
		print ("5 ADC = %lf"%(ADC_Value[5]*5.0/0x7fffff))
		print ("6 ADC = %lf"%(ADC_Value[6]*5.0/0x7fffff))
		print ("7 ADC = %lf"%(ADC_Value[7]*5.0/0x7fffff))
		print ("\33[9A")
        
except :
	GPIO.cleanup()
	print ("\r\nProgram end     ")
	exit()
