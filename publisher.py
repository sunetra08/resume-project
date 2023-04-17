# python 3.6

import random
import time
import requests
from paho.mqtt import client as mqtt_client


def weather():
    api_key = "APIKEY__2"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = 'KOLKATA'

    complete_url = base_url + "appid=" + \
        'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]-273.25
        current_temperature = "{:.2f}".format(current_temperature)

        return current_temperature

    else:
        return(" City Not Found ")


broker = 'broker.emqx.io'
port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(10)
        msg = ("{temperature : "+str(weather())+"}")
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print("{temperature : "+str(weather())+"}")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
