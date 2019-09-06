#coding: utf-8
import time

sec = 0
minutes = 0
while True:
	minutes += 1	
	while True:
		print(sec)
		time.sleep(1)
		sec += 1 
		if sec == 60:
			sec = 0
			minutes = str(minutes)
			print("\n" + minutes + " MIN COMPLITE\n") 
			minutes = int(minutes)
			break


