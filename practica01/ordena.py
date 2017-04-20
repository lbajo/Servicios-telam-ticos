#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys,types,re

from argparse import ArgumentParser

def main():
  parser = ArgumentParser()
  parser.add_argument("-i","--input",
                  action="store", dest='input',
                  help="Se leerá el texto desde el fichero indicado en -i --input, por omisión la entrada estándar",
                  default=sys.stdin,nargs="?")
  parser.add_argument("-o","--output",
                  action="store", dest='output',
                  help="Escribirá el texto en el fichero indicando -o --output , por omisión la salida estándar",
                  default=sys.stdout,nargs="?")

  argumentos=parser.parse_args()

  try:
    if len(sys.argv)>2:
      fichero_in=open (argumentos.input,'r')
    elif len(sys.argv)<2:
      fichero_in=argumentos.input
    lista_de_listas=[]
    lista_de_sumas=[]
    lista_aux=[]
    contador=1
    for linea in fichero_in:
      pf=linea.index('\n')
      linea=linea[:pf]
      if ','==linea[pf-1:pf]:
        print "Línea número", contador,"incorrecta:",linea
        raise SystemExit
      if linea!='':
        lis=linea.split(',')
        for x in lis:
          try:
            y=int(x)
            pos=lis.index(x)
            lis[pos]=y
          except ValueError:
            print "Línea número", contador,"incorrecta:",linea
            raise SystemExit
        lista_de_listas.append(lis)
      else:
        nada=[]
      contador=contador+1

    for x in lista_de_listas:
      s=sum(x)
      lista_de_sumas.append(s)

    lista_de_sumas.sort()

    for x in lista_de_listas:
      s=sum(x)
      pos_lista=lista_de_listas.index(x)
      pos_ls=lista_de_sumas.index(s);
      lista_aux.insert(pos_ls,x)

  except IOError:
    print "No se permite leer de este fichero"
    raise SystemExit

  try:
    if len(sys.argv)>2:
      fichero_out=open (argumentos.output,'w')
    elif len(sys.argv)<2:
      fichero_out=argumentos.output

    for x in lista_aux:
      for y in x:
        z=str(y)
        posi=x.index(y)
        x[posi]=z

    for x in lista_aux:
        t= ",".join(x)
        if len(sys.argv)>2:
          fichero_out.write(t+"\n")
        elif len(sys.argv)<2:
          print t

  except IOError:
    print "No se permite escribir en este fichero"
    raise SystemExit


  fichero_in.close()
  fichero_out.close()

if __name__ == "__main__":
  main()

