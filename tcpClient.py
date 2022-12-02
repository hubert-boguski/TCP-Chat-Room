import socket
import threading

import os

serverName = '127.0.0.1'
serverPort = 11000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) # connecting to the ports
name = input("Enter your name")

def getMsgs():
    while 1:
        messages = clientSocket.recv(1024).decode('ascii')
        #clientSocket.send(name.encode('ascii'))
        print(messages)

def sendMsgs():
    while 1:
        text = input("Enter a message: ")
        #messageToSend = f"{name} {text}!"    
        clientSocket.send(text.encode('ascii'))

getMsgThread = threading.Thread(target=getMsgs)
getMsgThread.start()
sendMsgsThread = threading.Thread(target=sendMsgs)
sendMsgsThread.start()


