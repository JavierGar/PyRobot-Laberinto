# -*- coding: latin-1 -*-

from LinkedList import *

class QueueList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)  # utilizamos el init de LinkedList
    def push(self, data):
        # forzamos el caso que nos interesa de la funcion insertafter
        self._LinkedList__current = self._LinkedList__tail
        LinkedList.insertAfter(self, data)
    def pop(self):
        # tenemos en cuenta el caso de que la lista este vacia, y si no es asi
        if self._LinkedList__size > 0:
            # guardamos los datos del primer nodo, que devolveremos despues
            primero = LinkedList.getHead(self)
            # forzamos el current al primer nodo, para que la funcion remove lo borre
            self._LinkedList__current = self._LinkedList__head
            LinkedList.remove(self)
            return primero
        else:
            raise IndexError ('Llista buida')
    def head(self):
        return LinkedList.getHead(self)
    def purge(self):
        LinkedList.clear(self)
    def __len__(self):
        return self._LinkedList__size

