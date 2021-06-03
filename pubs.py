#!/usr/bin/env python
import time
import paho.mqtt.client as paho
import random

broker="127.0.0.1"
port = 1883
topicX = "p1/x"
topicY = "p1/y"

#create client object client1

client= paho.Client("client-000") 

print("connecting to broker ", port)
client.connect(broker, port)#connect

print("publishing ")

x = 5;
y = 5;

while( True):
	x = x + random.uniform(-1.0, 1.0)
	y = y + random.uniform(-1.0, 1.0)
	
	x_sent = "{:.2f}".format(x)
	y_sent = "{:.2f}".format(y)
	mes = x_sent + " " + y_sent
	
	#print("Sent to topic", topicX, ":", x_sent)
	#print("Sent to topic", topicY, ":", y_sent)
	
	print (mes)
	
	#publish
	client.publish("p1", mes) 
	#client.publish("p1/y", y_sent)
	
	time.sleep(4)
