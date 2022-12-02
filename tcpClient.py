import socket
import threading

import os

serverName = '127.0.0.1'
serverPort = 11000
name = input("Enter your name")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) # connecting to the ports

def getMsgs():
    while 1:
        messages = clientSocket.recv(1024).decode('ascii')
        clientSocket.send(name.encode('ascii'))
        print(messages)

def sendMsgs():
    while 1:
        messageToSend = f'{name}: {input("")}'    

clientSocket.send(name.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024)
print ('From Server:', modifiedSentence.decode('utf-8'))
clientSocket.close()


