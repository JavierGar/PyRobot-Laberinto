# -*- coding: latin-1 -*-
from LinkedList import *

class Tree(object):
    __slots__ = ['__root']
    class Node(object):
        __slots__ = ['__data', '__childs']
        def __init__(self, data):
            self.__data = data
            self.__childs = LinkedList ()
        def addChild(self, child):
            self.__childs.insertAfter(child)
        def getChilds(self):
            return self.__childs
        def getData(self):
            return self.__data
        def getChild(self, data):
            aux = False
            if not self.__childs.isEmpty(): #si no esta vacia movemos el current al head
                self.__childs.moveHead()
                while aux==False:
                    if self.__childs.getCurrent().getData() == data: #comprobamos si el current es el que buscamos
                        return self.__childs.getCurrent()  #y lo devolvemos
                    else:  #si no es asi
                        if self.__childs.getCurrent() != self.__childs.getTail():  #si no hemos comprobado toda la lista
                            self.__childs.moveNext()  #movemos el current
                        else:  #si lo hemos hecho
                            return None

            else:  #si esta vacia
                return None
        def __str__(self):
            return self.str_recursive('', True)
        def str_recursive(self, prefix, final):
            if final:
                contingut = prefix + '└── ' + str(self.__data) + '\n'
                mascara =   prefix + '    '
            else:
                contingut = prefix + '├── ' + str(self.__data) + '\n'
                mascara =   prefix + '│   '
            if self.__childs.size() > 0:
                self.__childs.moveHead()
                for idx in range(self.__childs.size() - 1):
                    contingut += self.__childs.getCurrent().str_recursive(mascara, False)
                    self.__childs.moveNext()
                contingut += self.__childs.getCurrent().str_recursive(mascara, True)
            return contingut
    def __init__(self):
        self.__root = self.Node(None)
    def build(self, filename):
        f = open(filename, 'r')
        for linia in filter(lambda x: len(x.split()) == 18, f.readlines()):
            self.add(linia.split())
        f.close()
    def add(self, features):
        nodo = self.__root #empezamos en la raiz
        for i in range (len(features)):
            if nodo.getChild(features[i]) == None: #si no encuentra el nodo
                nuevo = Tree.Node(features[i]) #lo añadimos como hijo
                nodo.addChild(nuevo)  #del nodo actual
                nodo = nuevo  #y seguiremos iterando a partir de este
            else :
                nodo = nodo.getChild(features[i])  #si existe , iteramos a partir de este
    def search(self, features):
        nodo = self.__root #empezamos en la raiz
        for i in range (len(features)):  #recorremos para buscar
            if nodo.getChild(features[i]) == None:  #si no existen
                raise IndexError ('No fill')
            else:
                nodo = nodo.getChild(features[i]) # iteramos a partir de este
        return nodo.getChilds().getCurrent().getData()
    def __str__(self):
        contingut = 'ROOT\n'
        if self.__root.getChilds().size() > 0:
            self.__root.getChilds().moveHead()
            for idx in range(self.__root.getChilds().size() - 1):
                contingut += self.__root.getChilds().getCurrent().str_recursive('', False)
                self.__root.getChilds().moveNext()
            contingut += self.__root.getChilds().getCurrent().str_recursive('', True)
        return contingut 

