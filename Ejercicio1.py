#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import sys
from pprint import pprint

fichero_perros = open('/home/dani/Documentos/perros.json','r')
perro = json.load(fichero_perros)
print "Ejercicio 1. Lista las distintas razas que hay"
print "Estas son las distintas razas de perros que hay:"

filas = len(perro["animales"]["animal"])
#312
lista_perro=[]
for i in xrange(1,filas):
	raza = perro["animales"]["animal"][i]["descripcion"]
	if not raza in lista_perro:
		lista_perro.append(raza)

for x in lista_perro:
	print x