# -*- coding: utf-8 -*-
import requests
from lxml import etree
from suds.client import Client

linea = raw_input("Introduzca una linea: ")

cliente = Client('http://www.infobustussam.com:9001/services/dinamica.asmx?wsdl', retxml=True)

respuesta = cliente.service.GetStatusLinea('%s' % linea)

raiz = etree.fromstring(respuesta.encode("utf-8"))	
raiz2 = raiz[0][0]

tempuri = "{http://tempuri.org/}"
pretty = etree.tostring(raiz2, pretty_print=True)

indice = raiz2.find(tempuri+"GetStatusLineaResult")
ncochesact = indice.find(tempuri+"activos")
ncoches2 = ncochesact.text
frecok = indice.find(tempuri+"frec_bien")
frecok2 = frecok.text
incigrav = indice.find(tempuri+"graves")
incigrav2 = incigrav.text

print " "
print "Número de coches activos: %s" % ncoches2
print "Número de coches con frecuencia correcta: %s" % frecok2
print "Número de incidencias graves: %s" % incigrav2
print " "
print "Datos oficiales de TUSSAM."
