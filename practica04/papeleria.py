#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys,json,os
from argparse import ArgumentParser

def imprimir(f_in):
	for x in f_in:
		print x['ref'],'  ', x['precio'],'     ', x['descripcion']

def main():
	parser = ArgumentParser()
	parser.add_argument("fichero", help="Fichero json", metavar="N")
	argumentos=parser.parse_args()

	fich=open (argumentos.fichero,'r')
	f_in=json.load(fich)
	print "Ref.     Precio     Descripción"
	print '-----------------------------------------'
	imprimir(f_in)
  	
	fich.close()

if __name__ == "__main__":
	main()