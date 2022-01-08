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
	x = float(2**23)
	ADC_Value = ADC.ADS1256_GetAll()
	time.sleep(2)	
	ADC_Value = ADC.ADS1256_GetAll()
	print ("0 ADC = ", ADC_Value[0] * 5.0 / x)
	time.sleep(2)
	ADC_Value = ADC.ADS1256_GetAll()
	print ("0 ADC = ", ADC_Value[0] * 5.0 / x)
	time.sleep(2)
	ADC_Value = ADC.ADS1256_GetAll()
	print ("0 ADC = ", ADC_Value[0] * 5.0 / x - 1.236)
	print ()
	print ()
	time.sleep(2)
	offset =  1.2335
	while(1):
		ADC_Value = ADC.ADS1256_GetAll()
		print ("0 ADC = %lf"%(ADC_Value[0]*5.0/0x7fffff - offset))
		print ("1 ADC = %lf"%(ADC_Value[1]*5.0/0x7fffff - offset))
		print ("2 ADC = %lf"%(ADC_Value[2]*5.0/0x7fffff - offset))
		print ("3 ADC = %lf"%(ADC_Value[3]*5.0/0x7fffff - offset))
		print ("4 ADC = %lf"%(ADC_Value[4]*5.0/0x7fffff - offset))
		print ("5 ADC = %lf"%(ADC_Value[5]*5.0/0x7fffff - offset))
		print ("6 ADC = %lf"%(ADC_Value[6]*5.0/0x7fffff - offset))
		print ("7 ADC = %lf"%(ADC_Value[7]*5.0/0x7fffff - offset))
		print ("\33[9A")
        
except :
	GPIO.cleanup()
	print ("\r\nProgram end     ")
	exit()
