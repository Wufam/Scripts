#coding: utf-8
import sys
import telnetlib

while True:
	welcome = input("Welcome to telnet (press Enter)")

	host = input("Enter IP host: ")
	port = input("Enter port: ")

	port = int(port)
	 
	telnet = telnetlib.Telnet(host , port)
	port = str(port)
	 
	print("Prot " + port + " is not block")
	
	answer = input("Retry? y/n: ")
	if answer == "n":
		print("Close")
		sys.exit()
		
