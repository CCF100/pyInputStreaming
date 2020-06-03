#!/usr/bin/python
import socket
import threading
#import pyxinput
from time import sleep
import pickle
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
        decodedServerData = pickle.loads(from_server)
        print("Raw Data:", decodedServerData)
        MyVirtual.set_value(decodedServerData)
def virtualController():
    MyVirtual = pyxinput.vController()
    #Set percent to false so values match the raw data from the server
   # MyVirtual.percent = False
    MyRead = pyxinput.rController(1)
    print(MyRead.gamepad)
'''   
    while True:
        #global decodedServerData
        # Init virtual XInput Controller
        
        MyVirtual.set_value('AxisLy', 0)

'''
# Execute all functions as threads
if __name__ == "__main__":
    #Create Threads
    t1 = threading.Thread(target=recvData, args=(ip, port))
    #t2 = threading.Thread(target=virtualController, args=())
t1.start()
#t2.start()
