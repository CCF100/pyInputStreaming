#!/usr/bin/python
# Import libraries
from inputs import devices
from inputs import get_gamepad
import threading
import socket
from termcolor import colored
import pickle
import re
# Define ip/port to use
ip = "192.168.122.1"
port = 2222
# Show available gamepads
print("Gamepads available:")
print(devices.gamepads)
#Define decimal formula
decimalFormula = "2/(32767 - -32768)*(event.state-32767)+1"
#Define globals
controllerData = ""
#Dictionary of of all possible values
controllerDataDict = {'AxisLx': 0, 'AxisLy': 0, 'AxisRx': 0, 'AxisRy': 0, 'BtnBack': 0, 'BtnStart': 0, 'BtnA': 0, 'BtnB': 0, 'BtnX': 0, 'BtnY': 0, 'BtnThumbL': 0, 'BtnThumbR': 0, 'BtnShoulderL': 0, 'BtnShoulderR': 0, 'Dpad': 0, 'TriggerL': 0, 'TriggerR': 0}
#Lookup table to convert values from the "inputs" library
lookup_table = {'BTN_SELECT': 'BtnBack', 'BTN_START': 'BtnStart', 'BTN_SOUTH': 'BtnA', 'BTN_EAST': 'BtnB', 'BTN_NORTH': 'BtnX', 'BTN_WEST': 'BtnY', 'BTN_THUMBL': 'BtnThumbL', 'BTN_THUMBR': 'BtnThumbR', 'BTN_TL': 'BtnShoulderL', 'BTN_TR': 'BtnShoulderR'}
def sendData():
    #Pickle for transmittion
    pickle.dump(controllerDataDict, file)
    file.flush()
#Create Socket
socket = socket.create_server((ip, port))
#Wait for connections before continuing
print("Waiting for connection...")
connection, _ = socket.accept()
#Create pickler :D
file = connection.makefile(mode='wb')
pickler = pickle.Pickler(file)
file.flush()
print(connection)
print(type(connection))
#Immutible socket? I don't think so...
iwantThatRaddr = re.findall(r"'(?<=raddr=\(')\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'", str(connection))
print(iwantThatRaddr)
print(colored('Connected by', 'red'), iwantThatRaddr[0])
print(controllerDataDict)
while True:
        events = get_gamepad()
        for event in events:
            #controllerDataTuple = event.ev_type, event.code, event.state
            controllerDataTuple = event.code, event.state
            controllerData = controllerDataTuple
            print(controllerData)
            print(controllerDataDict)
            #If event.code is SYN_REPORT, ignore it
        if event.code == "SYN_REPORT":
            continue
        if event.code == "BTN_MODE":
            print(colored('The home button is unimplemented on PYXinput, ignoring', 'red'))
            continue
        #Ugh, PYXinput and inputs handle the Dpad in the most annoying way possible
        elif event.code == "ABS_HAT0X":
            #if ABS_HAT0X is 0, then there is no input on the dpad
            if event.state == 0:
                controllerDataDict['Dpad'] = 0  #No input
            if event.state == 1:
                controllerDataDict['Dpad'] = 8  #Right
            if event.state == -1:
                controllerDataDict['Dpad'] = 4  #Left
            sendData()
        elif event.code == "ABS_HAT0Y":
            #if ABS_HAT0Y is 0, then there is no input on the dpad
            if event.state == 0:
                controllerDataDict['Dpad'] = 0  #No input
            if event.state == 1:
                controllerDataDict['Dpad'] = 2  #Down
            if event.state == -1:
                controllerDataDict['Dpad'] = 1  #Up
            sendData()
        # The joysticks and triggers' values need to be normalized before they are sent
        #'ABS_X': 'AxisLx', 'ABS_Y': 'AxisLy', 'ABS_RX': 'AxisRx', 'ABS_RY': 'AxisRy'
        #Left Joystick
        elif event.code == 'ABS_X': # Left Joystick, left+right
            controllerDataDict['AxisLx'] = 2/(32767 - -32768)*(event.state-32767)+1
            sendData()
        elif event.code == 'ABS_Y': # Left Joystick, up+down
            controllerDataDict['AxisLy'] = - 2/(32767 - -32768)*(event.state-32767)+1-2
            sendData()
        #Right Joystick
        elif event.code == 'ABS_RX': # Left Joystick, left+right
            controllerDataDict['AxisRx'] = 2/(32767 - -32768)*(event.state-32767)+1
            sendData()
        elif event.code == 'ABS_RY': # Left Joystick, up+down
            controllerDataDict['AxisRy'] = - 2/(32767 - -32768)*(event.state-32767)+1-2
            sendData()
        #Now, for the triggers
        #'ABS_Z': 'TriggerL', 'ABS_RZ': 'TriggerR'
        elif event.code == 'ABS_Z':
            controllerDataDict['TriggerL'] = float(event.state) / 1023
            sendData()
        elif event.code == 'ABS_RZ':
            controllerDataDict['TriggerR'] = float(event.state) / 1023
            sendData()
        else:
            # Add button values to controllerDataDict
            controllerDataDict[lookup_table[str(event.code)]] = event.state
            sendData()
