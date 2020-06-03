#!/usr/bin/python
import socket
import threading
import re
import pyxinput
from time import sleep
# Define server ip and port
ip = '192.168.122.1'
port = 2222
#Define globals
decodedServerData = ""
def recvData(ip, port):
    global decodedServerData
    # Connect to Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #client.setblocking(False)
    client.connect((ip, port))
    while True:
        from_server = client.recv(4096)
        #Decode Sever message
        decodedServerData = from_server.decode()
        print("Raw Data:", decodedServerData)
def virtualController():
    MyVirtual = pyxinput.vController()
    MyRead = pyxinput.rController(1)
    print(MyRead.gamepad)
   
    while True:
        #global decodedServerData
        # Init virtual XInput Controller
        #print(MyRead.gamepad)
        MyVirtual.set_value('BtnA', 1)
        print(MyRead.buttons)
        sleep(3)
        #print(MyRead.gamepad)
        MyVirtual.set_value('BtnA', 0)
        print(MyRead.buttons)
        sleep(3)
# Execute all functions as threads
if __name__ == "__main__":
    #Create Threads
    t1 = threading.Thread(target=recvData, args=(ip, port))
    t2 = threading.Thread(target=virtualController, args=())
#t1.start()
t2.start()
