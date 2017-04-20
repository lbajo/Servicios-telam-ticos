#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import os,shutil,sys,unicodedata

from argparse import ArgumentParser

def existe_directorio(d):
  if os.path.isdir(d):
    return True
  else:
    return False

def obtener_lista(argumentos,direct,lista_dir):
  lista_new=[]
  for arch in lista_dir:
    if argumentos.spaces==True:
      arch=reemplazar_espacios(arch)
    elif argumentos.case==True:
      arch=reemplazar_mayusc(arch)
    elif argumentos.enne ==True:
      arch=reemplazar_enne(arch)
    elif argumentos.accent==True:
      arch=reemplazar_tildes(arch)
    elif argumentos.weird==True:
      arch=reemplazar_raros(arch)
    elif argumentos.recursive==True:
      arch=reemplazar_espacios(arch)
      arch=reemplazar_mayusc(arch)
      arch=reemplazar_enne(arch)
      arch=reemplazar_tildes(arch)
      arch=reemplazar_raros(arch)
    elif argumentos.spaces==False and argumentos.case==False and argumentos.enne ==False and argumentos.accent==False and argumentos.weird==False:
      arch=reemplazar_espacios(arch)
      arch=reemplazar_mayusc(arch)
      arch=reemplazar_enne(arch)
      arch=reemplazar_tildes(arch)
      arch=reemplazar_raros(arch)
    lista_new.append(arch)
  return lista_new

def cambiar_nombre(argumentos,direct,arch):
  if argumentos.spaces==True:
    arch=reemplazar_espacios(arch)
  elif argumentos.case==True:
    arch=reemplazar_mayusc(arch)
  elif argumentos.enne ==True:
    arch=reemplazar_enne(arch)
  elif argumentos.accent==True:
    arch=reemplazar_tildes(arch)
  elif argumentos.weird==True:
    arch=reemplazar_raros(arch)
  elif argumentos.recursive==True:
    arch=reemplazar_espacios(arch)
    arch=reemplazar_mayusc(arch)
    arch=reemplazar_enne(arch)
    arch=reemplazar_tildes(arch)
    arch=reemplazar_raros(arch)
  elif argumentos.spaces==False and argumentos.case==False and argumentos.enne ==False and argumentos.accent==False and argumentos.weird==False:
    arch=reemplazar_espacios(arch)
    arch=reemplazar_mayusc(arch)
    arch=reemplazar_enne(arch)
    arch=reemplazar_tildes(arch)
    arch=reemplazar_raros(arch)
  return arch
  

def recorrer(argumentos,direct,lista_dir,lista_nomod):
  for arch in lista_dir:
    arch_new=cambiar_nombre(argumentos,direct,arch)
    if arch in lista_nomod:
      continue
    if arch_new in lista_nomod:
      print 'El archivo', arch,'no se va a renombrar por riesgo de colisión'
    else:
      os.rename(arch,arch_new)
      lista_nomod.append(arch_new)


def reemplazar_espacios(arch):
  return arch.replace(' ','_')

def reemplazar_mayusc(arch):
  return arch.lower()

def reemplazar_enne(arch):
  return arch.replace(u'ñ',u'nn')

def reemplazar_tildes(arch):
  arch=arch.replace(u'á','a')
  arch=arch.replace(u'é','e')
  arch=arch.replace(u'í','i')
  arch=arch.replace(u'ó','o')
  arch=arch.replace(u'ú','u')
  return arch

def reemplazar_raros(arch):
  arch=arch.replace(u'¨','_')
  arch=arch.replace(u'-','_')
  arch=arch.replace(u'~','_')
  arch=arch.replace(u"#",'_')
  arch=arch.replace(u"@",'_')
  arch=arch.replace(u"|",'_')
  arch=arch.replace(u"!",'_')
  arch=arch.replace(u"·",'_')
  arch=arch.replace(u"$",'_')
  arch=arch.replace(u"%",'_')
  arch=arch.replace(u"&",'_')
  arch=arch.replace(u"/",'_')
  arch=arch.replace(u"(",'_')
  arch=arch.replace(u")",'_')
  arch=arch.replace(u"?",'_')
  arch=arch.replace(u"¡",'_')
  arch=arch.replace(u"¿",'_')
  arch=arch.replace(u"[",'_')
  arch=arch.replace(u"^",'_')
  arch=arch.replace(u"<code>",'_')
  arch=arch.replace(u"]",'_')
  arch=arch.replace(u"+",'_')
  arch=arch.replace(u"}",'_')
  arch=arch.replace(u"{",'_')
  arch=arch.replace(u"¨",'_')
  arch=arch.replace(u"´",'_')
  arch=arch.replace(u">",'_')
  arch=arch.replace(u"< ",'_')
  arch=arch.replace(u";",'_')
  arch=arch.replace( u",",'_')
  return arch
  

def procesar_directorio(argumentos,direct,direct_inicial):
    
  direct_intro=direct
  lista_dir=os.listdir(direct)

  #print direct
  #print lista_dir
  direct=os.chdir(direct_intro)

  lista_p=obtener_lista(argumentos,direct,lista_dir)
  #print lista_p
  lista_nomod=[]
  a=0
  while a<len(lista_dir):
    if lista_dir[a]==lista_p[a]:
      lista_nomod.append(lista_p[a])
    a=a+1
  #print lista_nomod
  recorrer(argumentos,direct,lista_dir,lista_nomod)

  direct=os.chdir(direct_inicial)

def main():
  parser = ArgumentParser()
  parser.add_argument("directorio", help="Directorio o directorios",nargs="*")
  parser.add_argument("-r","--recursive",
                  action="store_true", dest='recursive',
                  help="Recorrer los directorios rescursivamente",
                  default='stdout')
  parser.add_argument("-s","--spaces",
                  action="store_true", dest='spaces',
                  help="Reemplaza los espacios por barra baja",
                  default='stdout')
  parser.add_argument("-c","--case",
                  action="store_true", dest='case',
                  help="Reemplazar las mayúsculas por minúsculas",
                  default='stdout')
  parser.add_argument("-n","--enne",
                  action="store_true", dest='enne',
                  help="Reemplazar las eñe por otra combinación de letras",
                  default='stdout')
  parser.add_argument("-t","--accent",
                  action="store_true", dest='accent',
                  help="Reemplazar las vocales por acento",
                  default='stdout')
  parser.add_argument("-w","--weird",
                  action="store_true", dest='weird',
                  help="Reemplaza los caracteres raros",
                  default='stdout')

  argumentos=parser.parse_args()

  ad=argumentos.directorio
  if len(sys.argv)<2:
      print "Trabajamos sobre el directorio actual"
      direct_inicial=os.getcwd()
      procesar_directorio(unicode(direct_inicial),unicode(direct_inicial))
  else:
    for direct in ad:
      exists=existe_directorio(direct)
      if exists==False:
        print "El directorio",direct,"no existe, inténtelo de nuevo"
        raise SystemExit
      else:
        direct_inicial=os.getcwd()
        procesar_directorio(argumentos,unicode(direct),unicode(direct_inicial))

if __name__ == "__main__":
  main()