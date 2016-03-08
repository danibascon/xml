#!/usr/bin/python
# -+- coding: utf-8 .*.

import os
import sys
from lxml import etree

arbol = etree.parse("/home/dani/Documentos/eventos.xml")
raiz = arbol.getroot()


print "Duración de cada evento"
print ""

atributos = raiz.xpath('///atributos')
for x in atributos:
	nombre = x.xpath('atributo[2]/text()')
	duracion = x.xpath('atributo[4]/text()')
	for a,b in zip(nombre,duracion):
		print "El evento: ",a,"dura un total de",b,"horas"
print "Los eventos que tengan 0 horas, son aquellos de larga duracion"