import paho.mqtt.client as mqtt

def msgCallback(client, userdata, message):
    print(message.payload)

sub = mqtt.Client(client_id="subscriber")
sub.on_message = msgCallback

sub.connect(host = "192.168.0.175")
sub.subscribe("/test")

sub.loop_forever()
