import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin=17

GPIO.setup(led_pin,GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " +str(rc))
    client.subscribe("set")
    GPIO.output(led_pin, GPIO.HIGH) 
    client.publish("test", "OFF") 

def on_message(client, userdate, msg):
	if msg.payload.decode() == "ON":
		print("LED ON")
		GPIO.output(led_pin, GPIO.LOW)
		client.publish("test","ON")
	else:
		if msg.payload.decode() == "OFF":
			print("LED OFF")
			GPIO.output(led_pin, GPIO.HIGH)
			client.publish("test", "OFF")

client = mqtt.Client()
client.connect("192.168.1.116", 1883,  60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
