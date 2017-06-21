# -*- coding: latin-1 -*-

from LinkedList import *

class StackList(object):
    __slots__ = ['__llista']
    def __init__(self):
        self.__llista = LinkedList()
    def push(self, data):
        #si hacemos un insertBefore siempre insertaremos en la primera posicion ya
        #que el current siempre esta en el head si no lo movemos
        self.__llista.insertBefore(data)
    def pop(self):
        primero = self.__llista.getHead()  # cogemos la informacion del head
        self.__llista.remove()             # que será el ultimo que hemos añadido
        return primero                     # y luego borramos
    def head(self):
        primero = self.__llista.getHead()
        return primero
    def purge(self):
        self.__llista.clear()
    def __len__(self):  # devuelve el numero de elementos
        return self.__llista.size()
    def __str__(self):  # devuelve el contenido
        return self.__llista.__str__()

