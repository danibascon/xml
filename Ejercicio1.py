#!/usr/bin/python
# -+- coding: utf-8 .*.

import os
import sys
from lxml import etree

arbol = etree.parse("/home/dani/Documentos/eventos.xml")
raiz = arbol.getroot()


print "Ejercicio 1. Lista los distintos eventos"
print ""
print "Los eventos que hay son:"

contenido = raiz.findall('contenido/atributos')
for x in contenido:
	print "Evento:",x.xpath("atributo/text()")[1]