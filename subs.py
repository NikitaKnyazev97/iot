#!/usr/bin/env python
import time
import paho.mqtt.client as paho
from influxdb import InfluxDBClient
from queue import Queue

INFLUXDB_ADDRESS = '127.0.0.1'
INFLUXDB_USER = 'telegraf'
INFLUXDB_PASSWORD = 'telegraf'
INFLUXDB_DATABASE = 'people'

influxdb_client = InfluxDBClient(INFLUXDB_ADDRESS, 8086, INFLUXDB_USER, INFLUXDB_PASSWORD, database=INFLUXDB_DATABASE)


def send_sensor_data_to_influxdb(coords) -> None:
    """
    создает JSON для отправки в influxdb
    """
    json_body = [
        {
            "measurement": "p1",
            "fields": {
                "x": float(coords[0]),
                "y": float(coords[1])
            }
        }
    ]
    influxdb_client.write_points(json_body)
    return None


broker="127.0.0.1"
port = 1883

#define callback
def on_message(client, userdata, message):
	mes = message.payload.decode("utf-8")
	print("received message =", mes.split())
	q.put(mes.split())
    
    
q = Queue()
#init_influxdb_database()

#create client objects
client1= paho.Client("client-001") 

######Bind function to callback
client1.on_message=on_message

#####
print("connecting to broker ", broker, ":", port)

#connect
client1.connect(broker, port)

#start loop to process received messages
client1.loop_start() 

print("subscribing ")
client1.subscribe("p1")

#subscribe

while True:
	time.sleep(4)
	client1.on_message = on_message
	
	while not q.empty():
		message = q.get()
		send_sensor_data_to_influxdb(message)
		if message is None:
			continue
		print("received from queue", message)
	time.sleep(4)



