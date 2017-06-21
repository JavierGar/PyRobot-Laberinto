# -*- coding: latin-1 -*-


class LinkedList(object):
    __slots__ = ['__head', '__tail', '__current', '__size']
    class Node(object):
        __slots__ = ['__data', '__next']
        def __init__(self, data, next = None):
            self.__data = data
            self.__next = next
        def getData(self):
            return self.__data
        def getNext(self):
            return self.__next
        def setData(self, data):
            self.__data = data
        def setNext(self, next):
            self.__next = next
        def __str__(self):
            return str(self.__data)
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__current = None
        self.__size = 0
    def getHead(self):
        if self.__head is None:
            raise IndexError ('Llista buida')
        else: # devuelve el valor de data del primer nodo
            return self.__head.getData()
    def getTail(self):
        if self.__tail is None:
            raise IndexError ('Llista buida')
        else:  # devuelve el valor de data del ultimo nodo
            return self.__tail.getData()
    def getCurrent(self):
        if self.__current is None:
            raise IndexError ('Llista buida')
        else:  # devuelve el valor de data del nodo actual
            return self.__current.getData()
    def moveNext(self):
        if self.__current == self.__tail or self.__size == 0: #si la lista esta vacia, o el current esta en la ultima posicion
            raise IndexError ('Aquesta acció no es posible')  #este no se puede mover hacia adelante
        else :
            self.__current = self.__current.getNext()
    def moveHead(self):
        if self.__size == 0:
            raise IndexError ('Aquesta acció no es posible') #mueve el current al primer nodo, pero no puede si la lista
        else:                                                #está vacia
            self.__current = self.__head
    def isEmpty(self):
        if self.__size is 0:
            return True
        else:
            return False
    def size(self):
        return self.__size
    def clear(self):
        self.__head = None
        self.__tail = None
        self.__current = None
        self.__size = 0
    def insertBefore(self, data):
        if self.__head is None:
            temp = LinkedList.Node(data)
            temp.setNext(None)
            self.__head = temp
            self.__current = temp
            self.__tail = temp
            self.__size += 1
        elif self.__current == self.__head: #si el current es el primero hay que cambiar el head despues de insertar
            temp = LinkedList.Node(data)
            temp.setNext(self.__head)
            self.__head = temp
            self.__current = temp
            self.__size += 1
        else:
            temp = LinkedList.Node(data)
            rec = self.__head
            while rec.getNext()!= self.__current:
                rec = rec.getNext()
            rec.setNext(temp)
            temp.setNext(self.__current)
            self.__current = temp
            self.__size += 1
    def insertAfter(self, data):
        if self.__head is None:
            temp = LinkedList.Node(data)
            self.__head = temp
            self.__current = temp
            self.__tail = temp
            self.__size += 1
        elif self.__current == self.__tail: #si el current es el ultimo hay que cambiar el tail despues de insertar
            temp = LinkedList.Node(data)
            temp.setNext(None)
            self.__tail.setNext(temp)
            self.__tail = temp
            self.__current = temp
            self.__size += 1
        else:
            temp = LinkedList.Node(data)
            temp.setNext(self.__current.getNext())
            self.__current.setNext(temp)
            self.__current = temp
            self.__size += 1
    def remove(self):
        if self.__size == 0:
            raise IndexError ('Llista buida')
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
            self.__current = None
            self.__size = 0
        elif self.__current == self.__head: #si el current es el primero hay que cambiar el head para borrar
            self.__head = self.__current.getNext()
            self.__current = self.__current.getNext()
            self.__size -= 1
        elif self.__current == self.__tail: #si el current es el ultimo hay que cambiar el tail para borrar
            temp = self.__head
            while temp.getNext()!= self.__current:
                temp = temp.getNext()
            self.__tail = temp
            self.__tail.setNext(None)
            self.__current = self.__tail
            self.__size -= 1
        else:
            temp = self.__head
            while temp.getNext()!= self.__current:
                temp = temp.getNext()
            temp.setNext(self.__current.getNext())
            self.__current = temp
            self.__size -= 1
    def __str__(self):
        temp = self.__head
        list='LinkedList {'
        while temp is not None:
            list += temp.__str__()
            if (temp.getNext() is not None):
                list+= ', ' #concatena lo que va obteniendo separado por comas
            temp = temp.getNext()
        list += '}'
        return list



