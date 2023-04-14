import paho.mqtt.client as mqtt

# Define the callback function for when a message is received
def on_message(client, userdata, message):
    print("Received message:", str(message.payload.decode("utf-8")))

# Create an MQTT client instance
client = mqtt.Client()

# Set the callback function
client.on_message = on_message

# Connect to the broker
client.connect("4.193.183.143")

# Subscribe to the topic
client.subscribe("your_topic/temperature")

# Start the loop to listen for incoming messages
client.loop_forever()
