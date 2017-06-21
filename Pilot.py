# -*- coding: latin-1 -*- # Comentari per permetre que s'utilitzin accents i carÃ cters especials als comentaris i les cadenes de text.

from QueueList import *

class Pilot(object):
    __slots__ = ['__previous', '__sonar', '__inverse', '__culdesac']
    def __init__(self):
        self.__previous = None
        self.__sonar = {}
        self.__inverse = {'left' : 'right', 'right' : 'left', 'up' : 'down', 'down' : 'up'}
        self.__culdesac = False
    def getPrevious(self): return self.__previous
    def setSonar(self, sonar): self.__sonar = dict(sonar) # Fa una copia del diccionari, no una referÃ¨ncia.
    def isCrossRoad(self): return sum(self.__sonar.values()) > 2
    def getCulDeSac(self): return self.__culdesac
    def setCulDeSac(self, culdesac): self.__culdesac = culdesac

    def moveTo(self, action):
        #comprueba que el paramatro action es válido,si no es posible, crea una excepción
        if not action in ('left', 'right','up', 'down'):
            raise ValueError ('Acción no válida')
        #copia el diccionario del sonar, para buscar si la accion recibida es posible
        posibmoves = dict(self.__sonar)
        valid = posibmoves[action]
        if valid : #guarda la ultima accion invertida y devuelve action
            self.__previous = action
            #self.__previous = self.__inverse[action]
            return action
        #si no es posible, crea una excepción
        else:
            raise ValueError ('Acción imposible')

    def nextMove(self):
        # copiamos el sonar 
        moviments = dict(self.__sonar)
        # comprovamos si hay movimiento previo
        if not self.__previous is None:
            # si existe un movimiento previo, lo descartamos como movimiento posible
            moviments[self.__inverse[self.__previous]] = False
            # 4 false vol dir cul de sac, y volveriamos por donde hemos venido
        if moviments.values().count(False) == 4:
            self.setCulDeSac(True)
            action = self.__inverse[self.__previous]
            self.__previous = action
            return action
        else:
            # sino, cogemos la direccion posible
            for mov in moviments.keys():
                if moviments[mov] is True:
                    self.__previous = mov
                    print mov
                    return mov
        
    def possibleActions(self):
        lista = QueueList()
        moviments = dict(self.__sonar)  # guardamos el sonar
        if self.__previous != None:  # si hay movimiento previo lo guardamos
            tuplaprev = (True, self.__inverse[self.__previous])  # en el primer
            lista.push(tuplaprev)  # hueco de la cola con un true
        for mov in moviments:
            if mov != self.__inverse[self.__previous]:  # guardamos el resto de
                if moviments[mov] is True:  # movimientos, ignorando el previo
                    tuplamov = (False, mov)  # y con un false
                    lista.push(tuplamov)
        return lista
