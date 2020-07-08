# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Trab2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import random
import time

_translate = QtCore.QCoreApplication.translate


def bubble_sort(lista):
    for percorrer_lista in range(len(lista) - 1, 0, -1):
        for indice in range(percorrer_lista): 
            if lista[indice] > lista[indice + 1]:
                lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
    
    return lista

def selection_sort(lista):
    for indice in range(0, len(lista) - 1):
        valor_minimo = indice 
        for indice_posterior in range (indice + 1, len(lista)):  
            if (lista[indice_posterior] < lista[valor_minimo]): 
                valor_minimo = indice_posterior
        lista[indice],lista[valor_minimo] = lista[valor_minimo],lista[indice]

    return lista


def insertion_sort(lista):
    for indice in range(0,len(lista)):
        valor_indice = lista[indice] 
        indice_anterior = indice - 1
        while indice_anterior >= 0 and lista[indice_anterior] > valor_indice:
            lista[indice_anterior + 1] = lista[indice_anterior]
            indice_anterior -= 1
        lista[indice_anterior + 1] = valor_indice    

    return lista

def sort(lista):
    lista.sort()
    return lista




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(20, 20, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.Titulo.setFont(font)
        self.Titulo.setObjectName("Titulo")

        self.cemElementos = QtWidgets.QPushButton(self.centralwidget)
        self.cemElementos.setGeometry(QtCore.QRect(30, 60, 101, 23))
        self.cemElementos.setObjectName("cemElementos")
        self.cemElementos.clicked.connect(self.cemElementos_clicked)

        self.mil_elementos = QtWidgets.QPushButton(self.centralwidget)
        self.mil_elementos.setGeometry(QtCore.QRect(160, 60, 111, 23))
        self.mil_elementos.setObjectName("mil_elementos")
        self.mil_elementos.clicked.connect(self.milElementos_clicked)

        self.dezMilElementos = QtWidgets.QPushButton(self.centralwidget)
        self.dezMilElementos.setGeometry(QtCore.QRect(300, 60, 101, 23))
        self.dezMilElementos.setObjectName("dezMilElementos")
        self.dezMilElementos.clicked.connect(self.dezMilelementos_clicked)

        self.Bubble = QtWidgets.QLabel(self.centralwidget)
        self.Bubble.setGeometry(QtCore.QRect(30, 130, 141, 16))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)

        self.Bubble.setFont(font)
        self.Bubble.setObjectName("Bubble")
        self.Selection = QtWidgets.QLabel(self.centralwidget)
        self.Selection.setGeometry(QtCore.QRect(30, 160, 141, 16))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)

        self.Selection.setFont(font)
        self.Selection.setObjectName("Selection")

        self.Tempo_execucao = QtWidgets.QLabel(self.centralwidget)
        self.Tempo_execucao.setGeometry(QtCore.QRect(150, 100, 141, 16))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Tempo_execucao.setFont(font)
        self.Tempo_execucao.setObjectName("Tempo_execucao")
        self.Insertion = QtWidgets.QLabel(self.centralwidget)
        self.Insertion.setGeometry(QtCore.QRect(30, 190, 141, 16))

        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Insertion.setFont(font)
        self.Insertion.setObjectName("Insertion")

        self.sort = QtWidgets.QLabel(self.centralwidget)
        self.sort.setGeometry(QtCore.QRect(30, 220, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sort.setFont(font)
        self.sort.setObjectName("sort")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cemElementos_clicked(self):
        

        lista_aleatoria = random.sample(range(0, 100), 100)

        lista_bubble = lista_aleatoria.copy()
        lista_selection = lista_aleatoria.copy()
        lista_insertion = lista_aleatoria.copy()
        lista_func_sort = lista_aleatoria.copy()

        self.Titulo.setText("100 elementos: ")

        
        inicio_bubble = time.time()
        bubble_sort(lista_bubble)
        fim_bubble = time.time()
        """ tempo_round= round(fim_bubble - inicio_bubble, 7) """


        inicio_selection = time.time()
        selection_sort(lista_selection)
        fim_selection = time.time()


        inicio_insertion = time.time()
        insertion_sort(lista_insertion)
        fim_insertion = time.time()

        inicio_sort = time.time()
        sort(lista_func_sort)
        fim_sort = time.time()

        self.Bubble.setText(_translate("MainWindow", "Bubble: "+ str(round(fim_bubble - inicio_bubble, 7))))
        self.Selection.setText(_translate("MainWindow", "Selection: "+str(round(fim_selection - inicio_selection, 7))))
        self.Insertion.setText(_translate("MainWindow", "Insertion: "+str(round(fim_insertion - inicio_insertion, 7))))
        self.sort.setText(_translate("MainWindow", "Sort() :"+ str(round(fim_sort - inicio_sort,7))))

        print("bubble",round(fim_bubble - inicio_bubble, 7))
        print("selection: ",round(fim_selection - inicio_selection, 7))
        print("insertion: ",round(fim_insertion - inicio_insertion, 7))
        print("sort: ",(fim_sort - inicio_sort))
        

        
        self.update()

    def milElementos_clicked(self):

        lista_aleatoria = random.sample(range(0, 1000), 1000)

        lista_bubble = lista_aleatoria.copy()
        lista_selection = lista_aleatoria.copy()
        lista_insertion = lista_aleatoria.copy()
        lista_func_sort = lista_aleatoria.copy()

        self.Titulo.setText("1000 elementos: ")


        inicio_bubble = time.time()
        bubble_sort(lista_bubble)
        fim_bubble = time.time()


        inicio_selection = time.time()
        selection_sort(lista_selection)
        fim_selection = time.time()


        inicio_insertion = time.time()
        insertion_sort(lista_insertion)
        fim_insertion = time.time()

        inicio_sort = time.time()
        sort(lista_func_sort)
        fim_sort = time.time()

        self.Bubble.setText(_translate("MainWindow", "Bubble: "+ str(round(fim_bubble - inicio_bubble, 7))))
        self.Selection.setText(_translate("MainWindow", "Selection: "+str(round(fim_selection - inicio_selection, 7))))
        self.Insertion.setText(_translate("MainWindow", "Insertion: "+str(round(fim_insertion - inicio_insertion, 7))))
        self.sort.setText(_translate("MainWindow", "Sort() :"+ str(round(fim_sort - inicio_sort,7))))

        print("bubble",round(fim_bubble - inicio_bubble, 7))
        print("selection: ",round(fim_selection - inicio_selection, 7))
        print("insertion: ",round(fim_insertion - inicio_insertion, 7))
        print("sort: ",(fim_sort - inicio_sort))
        self.update()

    def dezMilelementos_clicked(self):



        lista_aleatoria = random.sample(range(0, 10000), 10000)

        lista_bubble = lista_aleatoria.copy()
        lista_selection = lista_aleatoria.copy()
        lista_insertion = lista_aleatoria.copy()
        lista_func_sort = lista_aleatoria.copy()

        self.Titulo.setText("10000 elementos: ")


        inicio_bubble = time.time()
        bubble_sort(lista_bubble)
        fim_bubble = time.time()


        inicio_selection = time.time()
        selection_sort(lista_selection)
        fim_selection = time.time()


        inicio_insertion = time.time()
        insertion_sort(lista_insertion)
        fim_insertion = time.time()

        inicio_sort = time.time()
        sort(lista_func_sort)
        fim_sort = time.time()

        self.Bubble.setText(_translate("MainWindow", "Bubble: "+ str(round(fim_bubble - inicio_bubble, 7))))
        self.Selection.setText(_translate("MainWindow", "Selection: "+str(round(fim_selection - inicio_selection, 7))))
        self.Insertion.setText(_translate("MainWindow", "Insertion: "+str(round(fim_insertion - inicio_insertion, 7))))
        self.sort.setText(_translate("MainWindow", "Sort() :"+ str(round(fim_sort - inicio_sort,7))))


        print("bubble",round(fim_bubble - inicio_bubble, 7))
        print("selection: ",round(fim_selection - inicio_selection, 7))
        print("insertion: ",round(fim_insertion - inicio_insertion, 7))
        print("sort: ",(fim_sort - inicio_sort))
        self.update()

    def update(self):
        self.Titulo.adjustSize()

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Titulo.setText(_translate("MainWindow", "Escolha o tamanho de sua lista:"))
        self.cemElementos.setText(_translate("MainWindow", "100 elementos"))
        self.mil_elementos.setText(_translate("MainWindow", "1000 elementos"))
        self.dezMilElementos.setText(_translate("MainWindow", "10000 elementos"))
        self.Tempo_execucao.setText(_translate("MainWindow", "Tempo de execução:"))
        self.Bubble.setText(_translate("MainWindow", "Bubble:"))
        self.Selection.setText(_translate("MainWindow", "Selection:"))
        self.Insertion.setText(_translate("MainWindow", "Insertion: "))
        self.sort.setText(_translate("MainWindow", "Sort() :"))


if __name__ == "__main__":
   
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
