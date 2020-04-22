import paho.mqtt.client as mqtt
import time

pub = mqtt.Client(client_id="publisher")

pub.username_pw_set("user", password="1234")
pub.connect(host = "192.168.0.175")

pub.loop_start()
i = 0
while True:
    msg = "Message #{}".format(i)
    pub.publish("/test", msg, qos=1, retain=True)
    i += 1
    time.sleep(0.5)
