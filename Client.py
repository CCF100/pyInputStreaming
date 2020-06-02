#!/usr/bin/python
import socket
import threading
import re
# Define server ip and port
ip = '127.0.0.1'
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
        
def printData():
    while True:
        global decodedServerData
        #print("Raw Data:", decodedServerData)
        #print('\n'+":O", end="\r", flush=True)

# Execute all functions as threads
if __name__ == "__main__":
    #Create Threads
    t1 = threading.Thread(target=recvData, args=(ip, port))
    t2 = threading.Thread(target=printData, args=())
t1.start()
t2.start()
