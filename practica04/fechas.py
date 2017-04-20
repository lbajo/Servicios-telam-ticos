#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import datetime,pytz,types,calendar,time,locale,sys,json
import xml.etree.cElementTree as ET

from argparse import ArgumentParser

def conv_xml(r,ra,num,fecha,entrada):
  elemento=ET.SubElement(r, u"instant")
  elemento.attrib={u"date":str(fecha), u"ordinal":str(num)}

def conv_json(num,fecha):
  try:
    c=fecha.index(',')
    fecha=fecha[:c]
    fl=fecha.index('\n')
    f=fecha[:fl]
    print json.dumps({num:f})

  except:
    try:
      fl=fecha.index('\n')
      f=fecha[:fl]
      print json.dumps({num:f})
    except:
      fecha=str(fecha)
      print json.dumps({num:fecha})

def trocear_mes(fecha):
    py=fecha.index('-')
    pm=fecha.index('-')
    mes=fecha[py+1:pm+3]
    mes=int(mes)
    #print mes
    return mes

def trocear_dia(fecha):
    pm=fecha.index('-')
    pd=fecha.index('-')+6
    pm=pm+4
    dia=fecha[pm:pd]
    dia=int(dia)
    #print dia
    return dia

def trocear_hora(fecha):
    ph=fecha.index(':')
    hora=fecha[ph-2:ph]
    hora=int(hora)
    #print hora
    return hora

def trocear_min(fecha):
    pmin=fecha.index(':')
    minut=fecha[pmin+1:pmin+3]
    minut=int(minut)
    #print minut
    return minut

def trocear_seg1(fecha):
    pmin=fecha.index(':')
    seg=fecha[pmin+4:]
    seg=int(seg)
    #print seg
    return seg

def trocear_seg2(fecha):
    pmin=fecha.index(':')
    pseg=fecha.index(',')
    seg=fecha[pmin+4:pseg]
    seg=int(seg)
    #print seg
    return seg

def trocear_ciudad(fecha):
    pc=fecha.index(',')
    pf=fecha.index('\n')
    ciudad=fecha[pc+2:pf]
    #print ciudad
    return ciudad

def unix(dt):
    ut=calendar.timegm(dt.utctimetuple())
    return ut

def calcular_zonas(year,mes,dia,hora,minut,seg,ciudad):
    utc=pytz.utc
    madrid = pytz.timezone("Europe/Madrid")
    londres= pytz.timezone("Europe/London")
    moscu= pytz.timezone("Europe/Moscow")
    tokio= pytz.timezone("Asia/Tokyo")
    new_york= pytz.timezone("America/New_York")
    zonas=["New_York", "Madrid", "Moscu", "Londres", "Tokio", "UTC"]
    for x in zonas:
        if ciudad==x:
          if x=="Madrid":
            dt1=datetime.datetime(year,mes,dia,hora,minut,seg)
            dt1=madrid.localize(dt1)
          elif x=="New_York":
            dt1=datetime.datetime(year,mes,dia,hora,minut,seg)
            dt1=new_york.localize(dt1)
          elif x=="Londres":
            dt1=datetime.datetime(year,mes,dia,hora,minut,seg)
            dt1=londres.localize(dt1)
          elif x=="Moscu":
            dt1=datetime.datetime(year,mes,dia,hora,minut,seg)
            dt1=moscu.localize(dt1)
          elif x=="Tokio":
            dt1=datetime.datetime(year,mes,dia,hora,minut,seg)
            dt1=tokio.localize(dt1)
          elif x=="UTC":
            dt1=datetime.datetime(year,mes,dia,hora,minut,seg)
            dt1=utc.localize(dt1)

    return dt1

def intro_ciudad(year,mes,dia,hora,minut,seg,x,cz):
  utc=pytz.utc
  madrid = pytz.timezone("Europe/Madrid")
  londres= pytz.timezone("Europe/London")
  moscu= pytz.timezone("Europe/Moscow")
  tokio= pytz.timezone("Asia/Tokyo")
  new_york= pytz.timezone("America/New_York")
  if x=="madrid":
    tz=cz.astimezone(madrid)
  elif x=="new_york":
    tz=cz.astimezone(new_york)
  elif x=="londres":
    tz=cz.astimezone(londres)
  elif x=="moscu":
    tz=cz.astimezone(moscu)
  elif x=="tokio":
    tz=cz.astimezone(tokio)
  elif x=="utc":
    tz=cz.astimezone(utc)   
  return tz

def main():
  parser = ArgumentParser()
  parser.add_argument("-t","--timezone",
                  action="store", dest='timezone',
                  help="Muestra por la salida estándar el número de línea y la hora dependiendo del formato que se le pase",
                  default='utc')
  parser.add_argument("-j","--json",
                  action="store_true", dest='json',
                  help="Muestra la salida en formato json")
  parser.add_argument("-a","--ascii",
                  action="store_true", dest='ascii',
                  help="Muestra la salida en texto plano")
  parser.add_argument("fichero", help="Fichero de fechas", metavar="N")

  argumentos=parser.parse_args()

  fin=open (argumentos.fichero,'r')

  at=argumentos.timezone

  zonas_comandos=["new_york", "madrid", "moscu", "londres", "tokio", "UTC"]

  fmt="%Y-%m-%d %H:%M:%S %Z%z"

  def trocear_year(fecha):
    py=fecha.index('-')
    if num >=10:
      year=fecha[pos-3:py]
    else:
      year=fecha[pos-2:py]
    year=int(year)
    return year

  root = ET.Element(u"instants")
  if argumentos.timezone=='epoch':
    root.attrib={u"city":'timestamp'}
  else:
    root.attrib={u"city":argumentos.timezone}

  for linea in fin:
    try:
      pos=linea.index(" ")+1
      num=linea[:pos]
      fecha=linea[pos:]
   
      num=int(num)

      year=trocear_year(fecha)
      mes=trocear_mes(fecha)
      dia=trocear_dia(fecha)
      hora=trocear_hora(fecha)
      minut=trocear_min(fecha)
      seg=trocear_seg2(fecha)
      ciudad=trocear_ciudad(fecha)

      #INTRODUCIMOS EPOCH
      if at=='epoch':
        dt=calcular_zonas(year,mes,dia,hora,minut,seg,ciudad)
        ut=unix(dt)
        if argumentos.json==False and argumentos.ascii==False: #salida en formato xml
          conv_xml(root, root.attrib,num,ut,'timestamp')
        elif argumentos.json==True: #json
          conv_json(num,ut)
        else:
          print num,ut

      #INTRODUCIMOS UNA CIUDAD
      if len(sys.argv)>2:
        for x in zonas_comandos:
          if at==x:
            dt=calcular_zonas(year,mes,dia,hora,minut,seg,ciudad)
            tz=intro_ciudad(year,mes,dia,hora,minut,seg,x,dt)
            if argumentos.json==False and argumentos.ascii==False: #formato xml
              conv_xml(root,root.attrib,num,tz,x)
            elif argumentos.json==True: #json
              conv_json(num,tz)
            else:
              print num,tz

      #SIN COMANDOS
      if len(sys.argv)<3:
        dt=calcular_zonas(year,mes,dia,hora,minut,seg,ciudad)
        utc=pytz.utc
        tz=dt.astimezone(utc)
        
        print num,tz

    except ValueError:
      try:
          finl=fecha.index('\n')
          timst=fecha[:finl]
          timst=int(timst)

          #INTRODUCIMOS EPOCH
          if at=='epoch':
            if argumentos.json==False and argumentos.ascii==False: #formato xml
              conv_xml(root,root.attrib,num,timst,'timestamp')
            elif argumentos.json==True: #json
              conv_json(num,timst)
            else:
              print num,timst


          #INTRODUCIMOS UNA CIUDAD 
          if len(sys.argv)>2: 
            for x in zonas_comandos:
              if at==x:
                tiimst=datetime.datetime.utcfromtimestamp(timst)
                tiimst=tiimst.strftime(fmt)
                year=trocear_year(tiimst)
                mes=trocear_mes(tiimst)
                dia=trocear_dia(tiimst)
                hora=trocear_hora(tiimst)
                minut=trocear_min(tiimst)
                seg=trocear_seg1(tiimst)
                cz=calcular_zonas(year,mes,dia,hora,minut,seg,"UTC")
                tz=intro_ciudad(year,mes,dia,hora,minut,seg,x,cz)
                if argumentos.json==False and argumentos.ascii==False: #formato xml
                  conv_xml(root,root.attrib,num,tz,x)
                elif argumentos.json==True: #json
                  conv_json(num,tz)
                else:
                  print num,tz

            #SIN COMANDOS
          if len(sys.argv)<3:
            tiimst=datetime.datetime.utcfromtimestamp(timst)
            tiimst=tiimst.strftime(fmt)
            year=trocear_year(tiimst)
            mes=trocear_mes(tiimst)
            dia=trocear_dia(tiimst)
            hora=trocear_hora(tiimst)
            minut=trocear_min(tiimst)
            seg=trocear_seg1(tiimst)
            cz=calcular_zonas(year,mes,dia,hora,minut,seg,"UTC")
            utc=pytz.utc
            tz=cz.astimezone(utc)
            print num,tz

      except ValueError:
        print 'Linea incorrecta'
        raise SystemExit

  if argumentos.json==False and argumentos.ascii==False and len(sys.argv)!=2 : #formato xml
    print ET.tostring(root, encoding="utf-8",method="xml")

  fin.close()

if __name__ == "__main__":
  main()

