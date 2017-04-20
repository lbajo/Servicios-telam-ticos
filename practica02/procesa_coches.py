#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys
import xml.etree.cElementTree as ET

from argparse import ArgumentParser

def imprimir(elemento):
	cab=[]
	e= elemento.attrib
	for x in e.keys():
		cab.append(e[x])
	print "       ".join(cab)
	for subelemento in elemento:
		imprimir(subelemento)

def main():
	parser = ArgumentParser()
	parser.add_argument("fichero", help="Fichero discoteca02.xml",default=sys.stdin, metavar="N",nargs="?")
	argumentos=parser.parse_args()
	
	root=ET.ElementTree(file=argumentos.fichero).getroot()
	print "Matricula   Modelo    Marca"
	print "----------------------------",
	imprimir(root)

if __name__ == "__main__":
	main()