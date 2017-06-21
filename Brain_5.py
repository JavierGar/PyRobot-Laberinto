# -*- coding: latin-1 -*- # Comentari per permetre que s'utilitzin accents i caràcters especials als comentaris i les cadenes de text.

from pyrobot.brain import Brain

from LinkedList import * # Es suposa que LinkedList està implementada correctament.
import StackList
reload(StackList) # 'reload' serveix per forçar a Python a carregar l'arxiu StackList i actualitzar-ne les possibles modificacions.
import Pilot
reload(Pilot)     # 'reload' serveix per forçar a Python a carregar l'arxiu Pilot i actualitzar-ne les possibles modificacions.
import Tree
reload(Tree)      # 'reload' serveix per forçar a Python a carregar l'arxiu Tree i actualitzar-ne les possibles modificacions.

class WB(Brain):
    def setup(self):
        self.stack = StackList.StackList()
        self.pilot = Pilot.Pilot()
        self.robot.move('reset')
        self.tree = Tree.Tree()
        self.tree.build('contrasenyes.txt')
        self.doors = {}
    def step(self):
        if not self.robot.getItem('win'):
            self.pilot.setSonar(self.robot.getItem('sonar'))
            if self.pilot.isCrossRoad():  # si es un cruce empieza el algoritmo backtracking
                if self.pilot.getCulDeSac()!= True or not self.stack:  #si es la primera vez que llegamos, o el stac
                    cross = self.pilot.possibleActions()  # esta vacio, lo llenamos
                    while cross:
                        pila = cross.pop()  # pasamos la cola a una pila, cambiando el orden
                        self.stack.push(pila)  # y poniendo la direccion por la que hemos llegado al final
                    tupla = self.stack.pop()
                    mov = self.pilot.moveTo(tupla[1])  # nos movemos donde nos indica la cola
                    self.pilot.setCulDeSac(tupla[0])   # y actualizamos la variable culdesac
                else :
                    tupla = self.stack.pop()  # si hay cosas en el stack
                    self.pilot.setCulDeSac(tupla[0])  # hacemos pop
                    mov = self.pilot.moveTo(tupla[1])
            # como no estamos en un cruce, nos movemos por el unico camino posible
            else:
                mov = self.pilot.nextMove()
            casilla = self.robot.move(mov)
            # solo intentamos recoger si hay oro
            if casilla == 'gold':
                self.robot.getItem('grab')
            if(casilla == 'door'):  # si estamos en una puerta
                print "puerta!"
                llista = []
                cont = []
                usada = False
                posicion = self.robot.getItem('location')
                if posicion in self.doors: #comprueba si hay una key que corresponda a nuestra posicion, lo que implica que la puerta ya ha sido interrogada
                    usada = True  #si es asi, usada es True para no volver a interrogar, y poder abrir

                if usada == False: #si es la primera vez que hablamos con la puerta
                    charla = self.robot.move('talk')  #igual que en la practica 3
                    while charla != None:  #hablamos con el objeto hasta que no tenga nada mas que decir
                        llista.append(charla)  #y vamos guardando lo que nos dice
                        charla = self.robot.move('talk')
                    self.doors[posicion] = llista #guardamos las palabras de cada puerta, y la key es la posicion

                else :
                    cont = self.doors[posicion]
                    word = self.tree.search(cont) #buscamos la palabra de la puerta
                    self.robot.move(word) #y la usamos

            elif (casilla=='key'):
                clave = []
                clau = self.robot.move('talk')  #igual que en la practica 3
                while (clau != "This thing doesn't speak!"):  #hablamos con el objeto hasta que no tenga nada mas que decir
                    print clau
                    clave.append(clau)  #y vamos guardando lo que nos dice
                    clau = self.robot.move('talk')
                self.tree.add(clave)  #guardamos la contraseña


def INIT(engine):
    return WB('WB', engine)
