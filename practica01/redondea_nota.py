#!/usr/bin/python -tt
# -*- coding: utf-8 -*-

nota=4.6;
modo="normal";

print "La nota del alumno es:", nota, " Modo:", modo

def redondea_nota(nota, modo):
	if modo== "normal":
		if nota<4.5:
			print "suspenso"
		elif nota>4.5 and nota<7:
			print "aprobado"
		elif nota>7 and nota<9:
			print "notable"
		elif nota>9 and nota<9.5:
			print "sobresaliente"
		elif nota>9.5:
			print "mención de honor"
	elif modo== "laxo":
		if nota<4:
			print "suspenso"
		elif nota>4 and nota<7:
			print "aprobado"
		elif nota>7 and nota<9:
			print "notable"
		elif nota>9 and nota<9.5:
			print "sobresaliente"
		elif nota==9.5:
			print "mención de honor"
		

	elif modo== "estricto":
		if nota<5:
			print "suspenso"
		elif nota>5 and nota<7:
			print "aprobado"
		elif nota>7 and nota<9:
			print "notable"
		elif nota>9 and nota<10:
			print "sobresaliente"
		elif nota==10:
			print "mención de honor"

redondea_nota(nota,modo)

