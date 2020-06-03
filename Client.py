#!/usr/bin/python
import socket
import threading
import pyxinput
from time import sleep
import pickle
# Define server ip and port
ip = '192.168.122.1'
port = 2222
# Create virtual controller
MyVirtual = pyxinput.vController()
# Connect to Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))
while True:
    from_server = client.recv(8144)
    #Decode Sever message
    decodedServerData = pickle.loads(from_server)
    print("Raw Data:", str(decodedServerData))
    # pyxinput will only accept values one at a time, so we need to apply the itme in the dictionary one by one
    for event, state in decodedServerData.items():
        MyVirtual.set_value(event, state)
        print('\''+event+'\''+',', state)
