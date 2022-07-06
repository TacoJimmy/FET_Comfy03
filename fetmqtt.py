import paho.mqtt.client as mqtt
import json  
import time
import readdata

client = mqtt.Client()


client.username_pw_set("BykBe22K0A3EdJOw7gxs","xxx")


client.connect("thingsboard.cloud", 1883, 60)


if __name__ == '__main__':
    while True:
        
        payload = {'Temp' : 20}
        print (json.dumps(payload))
        client.publish("v1/devices/me/telemetry", json.dumps(payload))
        time.sleep(5)