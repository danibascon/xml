#!/usr/bin/python
# -+- coding: utf-8 .*.

import sys
from lxml import etree

arbol = etree.parse("/home/dani/Documentos/eventos.xml")
raiz = arbol.getroot()


#1. Lista de eventos
print "Ejercicio 1. Lista los distintos eventos"
print ""
print "Los eventos que hay son:"

contenido = raiz.findall('contenido/atributos')
for x in contenido:
	print "Evento:",x.xpath("atributo/text()")[1]




#2. Contar los eventos por distritos
print "Ejercicio 2. Contar los eventos por distritos"
print ""




distrito = raiz.xpath('///atributos/atributo/atributo[10]/text()')
for x in distrito:
	print x
		

#3. Pedir por teclado un dia de la semana y mostrar los eventos de ese dia




dia = (raw_input("Dime un dia: ")).capitalize()[0]
fecha = raiz.xpath('///atributos/atributo[5]/text()')
dias = []

for x in fecha:
	if dia in x:
		dias.append(x)

print len(dias)











#4. Pedir dos fechas y mostrar los eventos que se realizan entre dichas fechas
#5. Duracion de cada evento










