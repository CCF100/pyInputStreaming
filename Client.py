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
conn = socket.create_connection((ip, port))
from_server = conn.makefile(mode='rb')
#Decode Sever message
#unpickler = pickle.Unpickler(file)
while True:
    #decodedServerData = unpickler.load()
    decodedServerData = pickle.load(from_server)
    #print("Raw Data:", from_server)
    #print("Unpicked Data: ", decodedServerData)
    # pyxinput will only accept values one at a time, so we need to apply the items in the dictionary one by one
    for event, state in decodedServerData.items():
        MyVirtual.set_value(event, state)
        #print('\''+event+'\''+',', state)
