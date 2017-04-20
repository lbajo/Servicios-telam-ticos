#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys,json,os,types
import xml.etree.cElementTree as ET
from argparse import ArgumentParser

inflacion=3

def imprimir(f_in):
	root = ET.Element(u"papeleria")
	for x in f_in:
		conv_xml(root,x['ref'],x['precio'],x['descripcion'])
	print ET.tostring(root, encoding="utf-8",method="xml")

def conv_xml(root,ref,precio,descripcion):
	elemento=ET.SubElement(root, u"objeto")
	precio=str(precio)
	precio.replace('.',' ')
	elemento.attrib={u"ref":str(ref),u"precio":precio,u"descripcion":descripcion}

def main():
	parser = ArgumentParser()
	parser.add_argument("fichero", help="Fichero json",default=sys.stdin, metavar="N",nargs="?")
	argumentos=parser.parse_args()

	fich=argumentos.fichero
	f_in=json.load(fich)
	imprimir(f_in)
  	
	fich.close()

if __name__ == "__main__":
	main()