#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys,types
import xml.etree.cElementTree as ET

#ESPECIFICAMENTE DISEÑADO PARA PROCESAR discoteca02.xml

from argparse import ArgumentParser

def imprimir_atb(elemento):
	cab=[]
	e= elemento.attrib
	for x in e.keys():
		cab.append(e[x])
	print"  /  ".join(cab)
	print "----------------------------------------------"

def imprimir_texto(elemento):
	print elemento.text


def main():
	parser = ArgumentParser()
	parser.add_argument("fichero", help="Fichero discoteca02.xml",default=sys.stdin, metavar="N", nargs="?")
	argumentos=parser.parse_args()
	
	root=ET.ElementTree(file=argumentos.fichero).getroot()
	for x in root:
		imprimir_atb(x)
		for y in x:
			imprimir_texto(y)

if __name__ == "__main__":
	main()