#!/usr/bin/python
# -+- coding: utf-8 .*.

import os
import sys
from lxml import etree

arbol = etree.parse("/home/dani/Documentos/eventos.xml")
raiz = arbol.getroot()


print "Ejercicio 1. Lista de los eventos que hay"
print "Ejercicio 2. Contar los eventos por distritos"
print "Ejercicio 3. Pedir por teclado un dia de la semana y mostrar los eventos de ese dia"
print "Ejercicio 4. Pedir dos fechas y mostrar los eventos que se realizan entre dichas fechas"
print "Ejercicio 5. Duracion de cada evento"

pregunta = int(raw_input("Dime el numero del ejercicio que quieres ejecutar: "))
os.system("clear")



	#1. Lista de eventos
if pregunta == 1:

	print "Ejercicio 1. Lista los distintos eventos"
	print ""
	print "Los eventos que hay son:"

	contenido = raiz.findall('contenido/atributos')
	for x in contenido:
		print "Evento:",x.xpath("atributo/text()")[1]




	#2. Contar los eventos por distritos
if pregunta == 2:

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



	#3. Pedir por teclado un dia de la semana y mostrar los eventos de ese dia
if pregunta == 3:


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



	#4. Pedir dos fechas y mostrar los eventos que se realizan entre dichas fechas
if pregunta == 4:


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


	#5. Duracion de cada evento
if pregunta == 5:
	print "Duración de cada evento"
	print ""

	atributos = raiz.xpath('///atributos')
	for x in atributos:
		nombre = x.xpath('atributo[2]/text()')
		duracion = x.xpath('atributo[4]/text()')
		for a,b in zip(nombre,duracion):
			print "El evento: ",a,"dura un total de",b,"horas"
	print "Los eventos que tengan 0 horas, son aquellos de larga duracion"








