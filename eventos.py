#!/usr/bin/python
# -+- coding: utf-8 .*.

from lxml import etree

doc=etree.parse('eventos.xml')
raiz=doc.getroot()

print "1. Listame los titulos de los eventos."
print "2. La cantidad de eventos que hay por distrito."
print "3. Mostrar los distrito donde aparezca la siguiente cadena."
print "4. Pedir distrito y mostrar los eventos que hay en cada uno."
print "5. Pedir una fecha de inico y otra de fin, y mostrar los eventos que empiecen y acaben en esa fecha."
print
print
lista_num=[1,2,3,4,5]
num=int(raw_input("Dime un ejercicio: "))
print
while num not in lista_num:
	num=int(raw_input("Dime un ejercicio entre el 1 y el 5: "))


print
print
if num==1:
	print "1. Listame los titulos de los eventos."
	print

	eventos= raiz.xpath('//atributo[@nombre="TITULO"]/text()')
	for x in set(eventos):
		print x
	print "hay un total de",len(eventos),"eventos"


if num==2:
	print "2. La cantidad de eventos que hay por distrito."
	print
	distrito=raiz.xpath('//atributo[@nombre="DISTRITO"]/text()')
	for x in set(distrito):
		print "distrito",x,"tiene un total de",distrito.count(x),"de eventos"
		


if num==3:
	print "3. Mostrar los distrito donde aparezca la siguiente cadena."
	print
	cadena=raw_input("Dime una cadena para buscar: ")
	lista_aux=[]
	lista_128=[]
	lista=raiz.xpath('//atributo/text()')

#esto lo hago porque si el caracter tiene mas de 128, me dará fallo, asi elimino, los elementos en lista,
#que tiene 128 o mas caracteres.
	cont =0
	for x in lista:
		if cadena in x:
			cont=cont+1
			lista_aux.append(x)

	for x in lista_aux:
		distrito=raiz.xpath('//atributo[.="'+x+'"]//..//../atributo[@nombre="DISTRITO"]/text()')

	if cont >0:
		print "En estos distritos se encuentra la cadena",cadena,":"
		for x in set(distrito):
			print x

	else:
		print "no existe esa cadena"




if num==4:
	print "4. Pedir distrito y mostrar los eventos que hay en cada uno."
	print

	cadena=raw_input("Dime un distrito: ").upper()
	lista=raiz.xpath('//atributo[.="'+cadena+'"]//..//../atributo[@nombre="TITULO"]/text()')

	print "El distrito",cadena,"tiene un total de",len(lista),"eventos:"
	for x in set(lista):
		print "   ~",x



if num==5:
	print "5. Pedir una fecha de inico y otra de fin, y mostrar los eventos que empiecen y acaben en esa fecha."
	print
	print

	yearini=int(raw_input("Dime el año de inicio (yyyy): "))
	while yearini < 2016:
		yearini=int(raw_input("Dime el año de inicio (yyyy) mayor que 2015: "))

	mesini=int(raw_input("Dime el mes de inicio (mm): "))
	while 1 > mesini or mesini > 12:
		mesini=int(raw_input("Dime el mes de inicio (mm) entre 1 y 12: "))


	print


	yearfin=int(raw_input("Dime el año de finalizacion (yyyy): "))
	while yearfin < 2016 or yearfin <yearini:
		yearfin=int(raw_input("Dime el año de finalizacion (yyyy) mayor que 2015 y mayor o igual que el de inicio: "))
	
	mesfin=int(raw_input("Dime el mes de finalizacion (mm): "))
	if yearini == yearfin:
		while 1 > mesfin or mesfin > 12 or mesfin < mesini:
			mesfin=int(raw_input("Dime el mes de finalizacion (mm) entre 1 y 12 y mayor o igual que el de inicio: "))
	if yearini < yearfin:
		while 1 > mesfin or mesfin > 12:
			mesfin=int(raw_input("Dime el mes de finalizacion (mm) entre 1 y 12: "))

	


	lista_fecha=[]
	inicio= raiz.xpath('//atributo[@nombre="FECHA-EVENTO"]/text()')
	fin= raiz.xpath('//atributo[@nombre="FECHA-FIN-EVENTO"]/text()')
	evento=raiz.xpath('//atributo[@nombre="TITULO"]/text()')


	for x,y,z in zip(inicio,fin,evento):
	   	lista_fecha.append([x,y,z])
	print
	print "Los eventos que comienzan",mesini,"-",yearini,"y acaban",mesfin,"-",yearfin,"son:"
	inicio=str(yearini)+"-0"+str(mesini)
	fin=str(yearfin)+"-0"+str(mesfin)
	cont=0
	for x in lista_fecha:
		if x[0][0:7] >=inicio and x[1][0:7]<=fin:
			cont=cont+1
			print x[2]
			print "  > inicio:",x[0]
			print "  > fin:",x[0]
	print
	if cont !=0:
		print "Hay un total de",cont,"eventos"
		
	else:
		print "No hay ningun evento durante esas fechas"
		

