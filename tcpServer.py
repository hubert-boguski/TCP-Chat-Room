# require a name for each connection
# then create a loop for each message with that connection
# so i need to seperate the initial connection with the message

#so start with a connection open and entering a name
#then create a loop with messages inside of it while keeping the connection 
import socket # importing library 
import threading
serverPort = 11000 # declaring open port for the server

users = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('',serverPort)) #Server is binded to the ip adresss and port 11000
server.listen() #starting listening mode
print ('We OPENNNN')

def msgToClients(msg):	
	for client in clients:
		client.send(msg) #while true, for each client, get the messages in the client

def updateServerWithMessage(client):
	while 1:
		msg = client.recv(1024)
		msgToClients(msg)

def getInfo():
	while 1:
		user, addr = server.accept()
		print ('Waiting for chatsss')
		user.send('Enter name:'.encode('ascii'))
		name = user.recv(1024).decode('ascii')
		
		names.append(name)

		msgToClients('{name} is now chattin. Give em a nice welcome!'.encode('ascii'))

		thread = threading.Thread(target=updateServerWithMessage, args=(client,))
		thread.start()

getInfo()