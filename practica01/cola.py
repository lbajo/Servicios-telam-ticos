#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

print "1.Creamos caja01 y caja02"

caja01= []
caja02= []

print "caja01 ", caja01
print "caja02 ", caja02

print "2.Añadimos los clientes"


caja01.append('Ernesto')
caja01.append('Paco')
caja01.append('Antonio')
caja01.append('Sergio')
caja02.append('Maria')
caja02.append('Lorena')
caja02.append('Pedro')
caja02.append('Marta')

print "caja01 ", caja01
print "caja02 ", caja02

print "3.Un cliente se va de la cola"

caja01.remove("Antonio")
print "caja01 ", caja01

print "4.Un cliente se pone primero"

caja01.remove("Sergio")
caja01.insert(0,"Sergio")
print "caja01 ", caja01

print "5.Abrimos la caja03 y pasan los de la caja02"

caja03=[]
caja02.remove("Lorena")
caja02.remove("Marta")
caja03.append("Lorena")
caja03.append("Marta")

print "caja02 ", caja02
print "caja03 ", caja03

print "6.Invertimos el orden de la caja01"

caja01.reverse()
print "caja01 ", caja01

print "7.Si hay un Ernesto en la caja01 se convierte en el primero de la cola"

cond= "Ernesto" in caja01
posicionErn=caja01.index('Ernesto')+1

if cond== True :

    caja01.remove("Ernesto")
    caja01.insert(0,"Ernesto")

    print "Ernesto pasa de la posicion ", posicionErn, "a la 1"
    print "caja01 ", caja01

else:

   print "Ernesto no está en la lista"


print "8.Creamos linea_de_cajas"

linea_de_cajas= [caja01, caja02, caja03]
print linea_de_cajas


print "9.Informe de cajas"

for x in linea_de_cajas:
    longit=len(x)
    print "Caja con ", longit, " clientes: ", ", ".join(x)

print "10.linea_de_cajas pasa a ser una lista de cadenas"

c1="; ".join(caja01)
c2="; ".join(caja01)
c3="; ".join(caja03)

linea_de_cajas= [c1,c2,c3]
print linea_de_cajas


