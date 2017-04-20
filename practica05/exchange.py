#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys,os,types,requests,json,datetime,time
import flask

CACHE_tiempo=0
resp_fixer=""
resp_cny=""
contador=0

timeout_bitcoin=300
timeout_divisas=86400

app=flask.Flask(__name__)

def consulta_btc():
	url='https://data.btcchina.com/data/ticker?market=btccny'
	r=requests.get(url)
	if r.status_code==200:
		texto=json.loads(r.content)
		return texto

def consulta_fixer():
	url='http://api.fixer.io/latest?base=CNY'
	r=requests.get(url)
	if r.status_code==200:
		texto=json.loads(r.content)
		return texto

def BTCCNY(texto):
	for x in texto.keys():
		ticker=texto['ticker']
	yu=ticker['buy']
		#print 'Para conseguir un bitcoin necesito:',yu,'yuanes'
	return yu

def CNYMON(moneda,texto):
	for x in texto.keys():
		rates=texto['rates']
	eu=rates[moneda]
		#print 'Para conseguir un yuan necesito', eu, 'euros'
	return eu

def obtener_cambio(cambio,texto):
	if cambio=='XBTEUR':
		return CNYMON('EUR',texto)
	elif cambio=='XBTGBP':
		return CNYMON('GBP',texto)
	elif cambio=='XBTCAD':
		return CNYMON('CAD',texto)
	elif cambio=='XBTJPY':
		return CNYMON('JPY',texto)
	elif cambio=='XBTAUD':
		return CNYMON('AUD',texto)
	elif cambio=='XBTCHF':
		return CNYMON('CHF',texto)
	elif cambio=='XBTRUB':
		return CNYMON('RUB',texto)

def trocear(cambio):
	if cambio=='XBTEUR':
		return 'EUR'
	elif cambio=='XBTGBP':
		return 'GBP'
	elif cambio=='XBTCAD':
		return 'CAD'
	elif cambio=='XBTJPY':
		return 'JPY'
	elif cambio=='XBTAUD':
		return 'AUD'
	elif cambio=='XBTCHF':
		return 'CHF'
	elif cambio=='XBTRUB':
		return 'RUB'

def caducado_bit(hora_inicial,hora_peticion):
	t_ult_pet=hora_inicial+timeout_bitcoin
	if t_ult_pet<hora_peticion:
		return True
	else:
		return False

def caducado_divisa(hora_inicial,hora_peticion):
	t_ult_pet=hora_inicial+timeout_divisas
	if t_ult_pet<hora_peticion:
		return True
	else:
		return False


@app.route('/exchange/<cambio>')
def exchange(cambio):
	global contador
	global CACHE_tiempo
	global resp_fixer
	global resp_cny

	query_string=flask.request.args
	if len(query_string)==1:
		divisa_peticion=time.time()
		if contador==0:
			cad=caducado_divisa(0,divisa_peticion)
			CACHE_tiempo=divisa_peticion
		else:
			cad=caducado_divisa(CACHE_tiempo,divisa_peticion)
		if cad==True:
			amount=query_string['amount']
			resp_fixer=consulta_fixer()
			c=obtener_cambio(cambio,resp_fixer)
			resp_cny=consulta_btc()
			yuanes=BTCCNY(resp_cny)
			bitalcambio=float(yuanes)*float(c)
			bitcoins_totales=bitalcambio*float(amount)
			tr=trocear(cambio)
			respuesta=json.dumps({cambio:bitalcambio,'XBT':amount,tr:bitcoins_totales},sort_keys=True, indent=4)
			CACHE_tiempo=divisa_peticion
		else:
			amount=query_string['amount']
			c=obtener_cambio(cambio,resp_fixer)
			yuanes=BTCCNY(resp_cny)
			bitalcambio=float(yuanes)*float(c)
			bitcoins_totales=bitalcambio*float(amount)
			tr=trocear(cambio)
			respuesta=json.dumps({cambio:bitalcambio,'XBT':amount,tr:bitcoins_totales},sort_keys=True, indent=4)
		contador=contador+1
		return respuesta
		
	else:	
		bit_peticion=time.time()
		cad=caducado_bit(CACHE_tiempo,bit_peticion)
		if contador==0:
			cad=caducado_bit(0,bit_peticion)
			CACHE_tiempo=bit_peticion
		else:
			cad=caducado_divisa(CACHE_tiempo,bit_peticion)
		if cad==True:
			resp_fixer=consulta_fixer()
			c=obtener_cambio(cambio,resp_fixer)
			resp_cny=consulta_btc()
			yuanes=BTCCNY(resp_cny)
			bitcoins=float(yuanes)*float(c)
			respuesta=json.dumps({cambio:bitcoins},True,4)
			CACHE_tiempo=bit_peticion

		else:
			c=obtener_cambio(cambio,resp_fixer)
			yuanes=BTCCNY(resp_cny)
			bitcoins=float(yuanes)*float(c)
			respuesta=json.dumps({cambio:bitcoins},True,4)
		contador=contador+1
		return respuesta

if __name__ == "__main__":
	app.run(debug=True)