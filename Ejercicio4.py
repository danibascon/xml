#!/usr/bin/python
# -+- coding: utf-8 .*.

import os
import sys
from lxml import etree

arbol = etree.parse("/home/dani/Documentos/eventos.xml")
raiz = arbol.getroot()

pedir_ano = int(raw_input("Dime un año: "))
while pedir_ano <=2014 or pedir_ano >= 2017:
	print "error, has metido mal el año"
	pedir_ano = int(raw_input("Dime bien el año: "))


pedir_mes = int(raw_input("Dime un mes: "))
while pedir_mes <=0 or pedir_mes >=13:
	print "error, has metido mal el mes"
	pedir_mes = int(raw_input("Dime bien el mes: "))



pedir_dia = int(raw_input("Dime un dia: "))
while pedir_dia <=0 or pedir_dia >=32:
	print "error, has metido mal el dia"
	pedir_dia = int(raw_input("Dime bien el dia: "))

fecha_pedir = [pedir_ano,pedir_mes,pedir_dia]
lista_fecha_inicio = []
lista_fecha_fin = []

atributos = raiz.xpath('///atributos')
lista_eventos_fecha =[]
lista_eventos = []
for x in atributos:
	fecha_fin = x.xpath('atributo[7]/text()')
	fecha_inicio = x.xpath('atributo[6]/text()')
	eventos_fecha2= x.xpath('atributo[2]/text()')

	for y in fecha_fin:
		contar_dia = len(y)
		if contar_dia < 10:
			fecha_fin = x.xpath('atributo[6]/text()')
			fecha_inicio = x.xpath('atributo[5]/text()')

			for z in fecha_fin:
				lista_fecha_fin.append(z[0:10])

			
			for z in fecha_inicio:
				lista_fecha_inicio.append(z[0:10])


		if contar_dia >= 10:
			for z in fecha_fin:
				lista_fecha_fin.append(z[0:10])
				
			for z in fecha_inicio:
				lista_fecha_inicio.append(z[0:10])
	lista_eventos.append(eventos_fecha2)
	
for a,b,c in zip(lista_fecha_inicio,lista_fecha_fin,lista_eventos):
	if fecha_pedir[0] >= a[0:4] and fecha_pedir[0] <= b[0:4]:
		if fecha_pedir[1] >= a[5:7] and fecha_pedir[1] <= b[5:7]:
			if fecha_pedir[2] >= x[8:10] and fecha_pedir[2] <=y[8:10]:
				print c
else:
	print "no hay ningun evento que se este celebrando en ese fecha en concreto"
