#!/usr/bin/python
# -+- coding: utf-8 .*.

import os
import sys
from lxml import etree

arbol = etree.parse("/home/dani/Documentos/eventos.xml")
raiz = arbol.getroot()

print "Ejercicio 2. Contar los eventos por distritos"
print ""

lista_distrito = []
distrito = raiz.xpath('///atributos/atributo/atributo[10]/text()')

for x in distrito:
	if not x in lista_distrito:
		lista_distrito.append(x)
		
for x in lista_distrito:
	cont = len(x)
	#15
for i in xrange(1,cont):
	conta = 0
	a = lista_distrito[i]
	for x in distrito:
		if a == x:
			conta = conta + 1
	print a,conta