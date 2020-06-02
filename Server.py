#!/usr/bin/python
# Import libraries
from inputs import devices
from inputs import get_gamepad
import threading
import socket
from termcolor import colored
# Define ip/port to use
ip = "127.0.0.1"
port = 2222
# Show available gamepads
print("Gamepads available:")
print(devices.gamepads)
#Define globals
controllerData = ""
# Show device output, send it in var
#def printInput():
    #global controllerData    
# Capture device input and send it via a web socket
#def inputCapture(ip, port):
    #global controllerData
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    s.listen(1)
    #s.setblocking(False)
    conn, addr = s.accept()
    with conn:
        print(colored('Connected by', 'red'), addr)
        while True:
            events = get_gamepad()
            for event in events:
                controllerDataTuple = event.ev_type, event.code, event.state
                controllerData = str(controllerDataTuple)
            print(controllerData)
            #Encode datastream for transmittion
            encodedControllerData=controllerData.encode()
            conn.send(encodedControllerData)
            #Wait for ok signal from client before continuing...
                





# Execute all functions as threads
#if __name__ == "__main__":
    #Create Threads
    #t1 = threading.Thread(target=printInput, args=())
    #t2 = threading.Thread(target=inputCapture, args=(ip, port))
#t1.start()
#t2.start()
