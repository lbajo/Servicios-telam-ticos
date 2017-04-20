#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys,os,types,requests,json
from argparse import ArgumentParser

def main():
	parser = ArgumentParser()
	parser.add_argument('-u','-user',action="store",dest='user',help="Muestra los mensajes correspondientes a este usuario",default=sys.stdin)
	argumentos=parser.parse_args()

	url='http://127.0.0.1:5000/exchange/XBTGBP?amount=5.23'
	r=requests.get(url)
	if r.status_code==200:
		print r.content
	

if __name__ == "__main__":
	main()