import paho.mqtt.client as mqtt
import base64
import json
import requests


client = mqtt.Client()
client.connect('mqtt.eclipseprojects.io')
client.subscribe("topic")


with open('2.json', 'rb') as file:
    f = file.read()

j = f
base64_bytes = base64.b64encode(j)
base64_m = base64_bytes.decode('ascii')

client.publish('topic', base64_m)
