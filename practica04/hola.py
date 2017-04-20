#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

import requests

# Este servicio de prueba nos devuelve nuestra direccion ip
url="http://httpbin.org/ip"

r=requests.get(url)
if r.status_code==200:
	print r.json() # {u'origin': u'81.37.7.200'}
else:
	print "error "+str(r.status_code)