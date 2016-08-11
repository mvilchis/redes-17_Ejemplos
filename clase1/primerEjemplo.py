#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys,getopt

"""
   Funcion que muestra como convertir un numero a 
   flotante
"""
def prueba_numeros():
    flotante = float(15)
    print "Numero: %s, tipo %s" %(flotante, type(flotante))
    numero = 15
    print "Numero: %s, tipo %s" %(numero, type(numero))

""" 
   Funcion que define como calcular el factorial de
   un numero, contando con un parametro por default 
"""
def fact(hasta=10):
    i = 1
    for idx in range(1,hasta):
        i *=idx
    return i 

"""
  Funcion que muestra como crear una cadena en python
  y el uso intercalado de comillas
""" 
def cadena():
    primer_cad = 'hola mundo'
    segunda_cad = "adios mundo"
    tercer_cad = "hola 'mundo'"
    print primer_cad
    print segunda_cad 
    print tercer_cad

"""
   Funcion que muestra los principales operadores 
   para valores numericos 
"""
def operadores():
    a = 10
    b = 5 
    print "Primer operando: %s" %(a)
    print "Segundo operando: %s" %(b)
    print "Operacion: + \n Resultado: %s (tipo: %s)\n" %(a+b, type(a+b))
    print "Operacion: - \n Resultado: %s (tipo: %s)\n" %(a-b, type(a-b))
    print "Operacion: * \n Resultado: %s (tipo: %s)\n" %(a*b, type(a*b))
    print "Operacion: / \n Resultado: %s (tipo: %s)\n" %(a/b, type(a/b))
    print "Operacion:mod  \n Resultado: %s (tipo: %s)\n" %(a%b, type(a%b))
    print "Operacion:pot  \n Resultado: %s (tipo: %s)\n" %(a**b, type(a**b))

"""
   Funcion que muestra como crear una lista e ir agregando elementos
"""
def lista():
    mi_lista = []
    mi_lista.append(1)
    mi_lista.append(2)
    mi_lista.append(3)
    mi_lista.append('a')
    mi_lista.append('b')
    for item in mi_lista:
        print  "Item: %s tipo(%s)" %(item, type(item))
    #print mi_lista*5
    pares = range(0, 50, 2)
    print  pares

"""
  Funcion que muestra el uso de is e in
"""
def condicionales():
    # ==
    # <= 
    # >= 
    nombres = ['alice', 'bob']
    nombre = 'alice'
    if nombre in nombres: 
      print "El nombre %s esta contenido en %s" %(nombre, nombres)
    nombres2 = ['alice', 'bob']
    print nombres == nombres2
    print nombres is nombres2
 
if __name__ == '__main__':
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "l", ["local="])
    ejercicio = args[0]
    if(ejercicio == 'numeros'):
        prueba_numeros()
    if ejercicio == 'fact':
        if len(args) > 1 :
           hasta = int(args[1]) 
           print "%s" %(fact(hasta))
        else: 
          print "%s" %(fact())
    if ejercicio == 'cad':
        cadena()
    if ejercicio == 'op':
        operadores()
    if ejercicio == 'lista':
        lista()
    if ejercicio == 'cond':
        condicionales()
