#!/usr/bin/python
# -+- coding: utf-8 .*.

import os
import sys
from lxml import etree

arbol = etree.parse("/home/dani/Documentos/eventos.xml")
raiz = arbol.getroot()

semana=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

dia2 = (raw_input("Dime un dia de la semana: ")).capitalize()

if not dia2 in semana:
	print "erro, no has introducido bien el dia"
	sys.exit()

lista_eventos_fecha= []

if dia2 == "Miercoles":
	dia2 = "X"

dia = dia2[0]
atributos = raiz.xpath('///atributos')

print "Los eventos que empiezan",dia2,"son:"
print ""

for x in atributos:
	fecha = x.xpath('atributo[5]/text()')
	eventos_fecha= x.xpath('atributo[2]/text()')
	
	for y in fecha:
		if dia in y:

			lista_eventos_fecha.append(eventos_fecha)

for x in lista_eventos_fecha:
	for y in x:
		print y


















