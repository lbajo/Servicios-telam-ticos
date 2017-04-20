#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

print "     (1)"

provincias={'Madrid':['cocido'],'Sevilla': ['gazpacho', 'pescaito'], 'Alicante': ['salmonetes', 'ensalada']}
print provincias

print "     (2)  "

provincias['Leon']=['morcilla', 'menestra']
provincias['CiudadReal']=['berenjenas','pisto']
print provincias

print "     (3)  "

provincias['Leon'].append('picadillo')
provincias['Madrid'].append('vino')
print provincias

print "     (4)  "

alcoholicas=['vino','sidra','cerveza']

for x in provincias.keys():
    for y in provincias[x]:
        if y in alcoholicas:
            provincias[x].remove(y);

print provincias;

print "     (5)  "  

comunidad_valenciana=['Valencia','Alicante','Castellon']

for x in provincias.keys():
    if x in comunidad_valenciana:
        provincias[x].append('paella')

print provincias

print "     (6)"

for x in provincias.keys():
    if x in comunidad_valenciana:
        del provincias[x];

print provincias


print "     (7)  "

def muestra_alfabetico(provincias):
    prov_cl=provincias.keys()
    prov_cl.sort()
    for cl in prov_cl:
         print cl,":", ", ".join(provincias[cl])  
muestra_alfabetico(provincias)

print "     (8)  "

def muestra_por_longitud(provincias):
    lista_p=[]
    lista_long=[]
    prov_cl=provincias.keys()
    for cl in prov_cl:
        lon=len(provincias[cl])
        lista_p.append(cl)
        lista_long.append(lon)
        pos_ls=lista_long.index(lon);
        lista_long.sort()
        print cl,":", ", ".join(provincias[cl]) 
 
muestra_por_longitud(provincias)