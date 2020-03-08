#!/usr/bin/python

"""
Cheked utils 'rm -rf or rm -r' for delete files
when not inode

"""
import subprocess

count = input("How count file: " )
count = int(count)
number = 1
for i in range (count):
	number = int(number)
	number += 1
	number = str(number)

	sub = subprocess.run(['touch', number])

