#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import types,sys

lista=[[1,3],[5],[0],[2,2,2]]
print "lista=", lista

for x in lista:
    for y in x:
        if type(y)!=types.IntType:
            print 'Hay un elemento no permitido'
            raise SystemExit 
if lista==[]: 
    print 'Lista vacía'
    raise SystemExit

lista_de_sumas=[]

for x in lista:
    s=sum(x)
    lista_de_sumas.append(s)

lista_de_sumas.sort()

lista_aux=[]

for x in lista:
    s=sum(x)
    pos_lista=lista.index(x)
    pos_ls=lista_de_sumas.index(s);
    lista_aux.insert(pos_ls,x)

print "lista_ordenada=", lista_aux




