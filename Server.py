#!/usr/bin/python
# Import libraries
from inputs import devices
from inputs import get_gamepad
import threading
import socket
from termcolor import colored
import pickle
# Define ip/port to use
ip = "192.168.122.1"
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
print("Waiting for connection...")
'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((ip, port))
    s.listen(1)
    #s.setblocking(False)
    conn, addr = s.accept()
    with conn:
        print(colored('Connected by', 'red'), addr)
'''
#Dictionary of of all possible values
controllerDataDict = {'AxisLx': 0, 'AxisLy': 0, 'AxisRx': 0, 'AxisRy': 0, 'BtnBack': 0, 'BtnStart': 0, 'BtnA': 0, 'BtnB': 0, 'BtnX': 0, 'BtnY': 0, 'BtnThumbL': 0, 'BtnThumbR': 0, 'BtnShoulderL': 0, 'BtnShoulderR': 0, 'Dpad': 0, 'TriggerL': 0, 'TriggerR,': 0}
# Convert "inputs" library data to our dict
print(controllerDataDict)
        #Print value of AxisRx
        #print(controllerDataDict['AxisRx'])
while True:
    events = get_gamepad()
    for event in events:
        #controllerDataTuple = event.ev_type, event.code, event.state
        controllerDataTuple = event.code, event.state
        controllerData = controllerDataTuple
        #print("controllerData is a", type(controllerData))
        print(controllerData)
        
'''
                #Pickle for transmittion
                encodedControllerData = pickle.dumps(controllerDataDict)
                print(encodedControllerData)
                conn.send(encodedControllerData)
                #Wait for ok signal from client before continuing...
'''





# Execute all functions as threads
#if __name__ == "__main__":
    #Create Threads
    #t1 = threading.Thread(target=printInput, args=())
    #t2 = threading.Thread(target=inputCapture, args=(ip, port))
#t1.start()
#t2.start()
