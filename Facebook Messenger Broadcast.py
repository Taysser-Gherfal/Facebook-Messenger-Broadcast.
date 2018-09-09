#!/usr/bin/env python3
#! python3

import os
from fbchat import Client
from fbchat.models import *

# Getting the user's account information
email = input("Enter your email: ")
password = input("Enter your password: ")
client = Client(email, password)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Reading your message...
print("Reading your message.txt...")
print()
message_file = open(os.path.join(os.path.dirname(__file__), 'message.txt'))
message = message_file.read()
message_file.close()

# Reading your friends list...
print("Reading data.txt...")
print()
friends = open(os.path.join(os.path.dirname(__file__), 'friends.txt'))
text = friends.read()
friends.close()

# Informing the user that their message is about to be sent...
print("Sending your message...")
print()
print(message)
print()

# Sending the message...
lines = text.split('\n')
for i in lines:
	try:
		users = client.searchForUsers(i)
		if users:
			user = users[0]
			print (user.uid +"-"+ user.name)
			client.send(Message(text= message), thread_id=user.uid, thread_type=ThreadType.USER)
	except:
		print("------Error with------" + user.name)
