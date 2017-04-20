#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys,json,os
from argparse import ArgumentParser

inflacion=3

def imprimir(f_in):
	for x in f_in:
		x['precio']=x['precio']*(1+(inflacion*0.01))
		print x['ref'],'  ', x['precio'],'     ', x['descripcion']

def main():
	parser = ArgumentParser()
	parser.add_argument("fichero", help="Fichero json",default=sys.stdin, metavar="N",nargs="?")
	argumentos=parser.parse_args()

	fich=argumentos.fichero
	f_in=json.load(fich)
	print "Ref.     Precio     Descripción"
	print '-----------------------------------------'
	imprimir(f_in)
  	
	fich.close()

if __name__ == "__main__":
	main()