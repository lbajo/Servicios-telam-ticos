#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import sys,os,types,requests,json

from argparse import ArgumentParser

def mensajes_totales():
	url='http://jsonplaceholder.typicode.com/users'
	r=requests.get(url)
	if r.status_code==200:
		texto=json.loads(r.content)
	for x in texto:
		uname=x['username']
		userId=x['id']
		url='http://jsonplaceholder.typicode.com/posts?userId='+str(userId)
		r=requests.get(url)
		texto=json.loads(r.content)
		for x in texto:
			print 'De:',uname
			title=x['title']
			body=x['body']
			print title 
			print '-----------------------------------------------'
			print body
			print ''

def existe_user(au,lista):
	cont=0
	for x in lista:
		if au==x:
			cont=cont+1;
		else:
			cont=cont+0
	if cont==0:
		return False
	else:
		return True

def mensajes_user(au):
	au=au.title()
	lista_users=[]
	url='http://jsonplaceholder.typicode.com/users'
	r=requests.get(url)
	if r.status_code==200:
		texto=json.loads(r.content)
	for x in texto:
		uname=x['username']
		lista_users.append(uname)

	bol=existe_user(au,lista_users)
	if bol==True:
		for x in texto:
			uname=x['username']
			userId=x['id']
			if au==uname:
				url='http://jsonplaceholder.typicode.com/posts?userId='+str(userId)
				r=requests.get(url)
				texto=json.loads(r.content)
				for x in texto:
					print 'De:',uname
					title=x['title']
					body=x['body']
					print title 
					print '-----------------------------------------------'
					print body
					print ''
	else:
		sys.stderr.write('El usuario introducido no existe \n') 
		raise SystemExit

			
def main():
	parser = ArgumentParser()
	parser.add_argument('-u','-user',action="store",dest='user',help="Muestra los mensajes correspondientes a este usuario",default=sys.stdin)
	argumentos=parser.parse_args()

	if len(sys.argv)<2:
		mensajes_totales()
	else:
		mensajes_user(argumentos.user)

if __name__ == "__main__":
	main()