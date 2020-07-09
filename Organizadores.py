#importando bibliotecas necessárias para funcionamento do código

import sys #modulo nativo do python para algumas variáveis usadas ou mantidas pelo interpretador
from PyQt5 import QtCore, QtGui, QtWidgets #framework em C++ para o desenvolvimento da UI
import random #gerador de números pseudo-aleatórios
import time #usado para análise do tempo de execução de para organizador

_translate = QtCore.QCoreApplication.translate #método para tradução



#método de organizador bolha
def bubble_sort(lista):
    for percorrer_lista in range(len(lista) - 1, 0, -1):
        for indice in range(percorrer_lista): 
            if lista[indice] > lista[indice + 1]:
                lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
    
    return lista

#método organizador de seleção
def selection_sort(lista):
    for indice in range(0, len(lista) - 1):
        valor_minimo = indice 
        for indice_posterior in range (indice + 1, len(lista)):  
            if (lista[indice_posterior] < lista[valor_minimo]): 
                valor_minimo = indice_posterior
        lista[indice],lista[valor_minimo] = lista[valor_minimo],lista[indice]

    return lista

#método organizador de inserção 
def insertion_sort(lista):
    for indice in range(0,len(lista)):
        valor_indice = lista[indice] 
        indice_anterior = indice - 1
        while indice_anterior >= 0 and lista[indice_anterior] > valor_indice:
            lista[indice_anterior + 1] = lista[indice_anterior]
            indice_anterior -= 1
        lista[indice_anterior + 1] = valor_indice    

    return lista

#método organizador nativo do python
def sort(lista):
    lista.sort()
    return lista


#função criada para facilitar o manejo das listas
def Listas(n):
    lista_aleatoria = random.sample(range(0, n), n) #gerador de funções pseudo-aleatórias com a biblioteca random

    global lista_bubble, lista_selection, lista_insertion, lista_func_sort #Essas listas foram definidas como globais para uso fora da função

    #As listas são cópias da lista_aleatoria para evitar póssiveis erros
    lista_bubble = lista_aleatoria.copy()
    lista_selection = lista_aleatoria.copy()
    lista_insertion = lista_aleatoria.copy()
    lista_func_sort = lista_aleatoria.copy()

#função criada para melhor organização da medição de tempo e organização das listas
def execucao_orcanizadores(Listas):

    global tempo_bubble, tempo_selection, tempo_insertion, tempo_sort #o tempo de execução foi definido como global para utilização fora da função

    #utilizando a função time.time(), pegamos o tempo de execução do programa no momento em que chamamos a função
    ini = time.time()
    bubble_sort(lista_bubble)
    fim = time.time()
    tempo_bubble = str(round(fim - ini, 7)) 
    #a variável foi definida como uma string pois o pyqt5 exige que para mostrar um número em seus label's, o mesmo seja uma str
    #foi utilizado o round() com 7 casas decimais para melhor leitura do tempo de execução no programa
    #subtraindo o tempo de execução de depois e antes da função do organizador, temos o tempo de execução daquela função


    ini = time.time()
    selection_sort(lista_selection)
    fim = time.time()
    tempo_selection = str(round(fim - ini, 7))

    ini = time.time()
    insertion_sort(lista_insertion)
    fim = time.time()
    tempo_insertion = str(round(fim - ini, 7))

    ini = time.time()
    sort(lista_func_sort)
    fim = time.time()
    tempo_sort = str(round(fim - ini, 7))


#criação da UI
class Ui_MainWindow(object):
    #inicializando a interface
    def setupUi(self, MainWindow):
        #MainWindow
        MainWindow.setObjectName("MainWindow")#definindo o nome do objeto para a janela principal
        MainWindow.resize(432, 283)#tamanho da interface

        #centralwidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)#definindo método para localização dos Widget
        self.centralwidget.setObjectName("centralwidget")#nome do objeto de localização

        #Titulo
        self.Titulo = QtWidgets.QLabel(self.centralwidget)#definindo o Widget "Titulo" como um label
        self.Titulo.setGeometry(QtCore.QRect(20, 20, 391, 31))#coordenadas(x,y) e tamanho(largura,altura) do Widgets "Titulo"
        font = QtGui.QFont()#definindo "font" como uma fonte
        font.setFamily("Arial")#definindo a família da "font" para "Arial"
        font.setPointSize(20)#tamanho da fonte
        self.Titulo.setFont(font)#definindo "Titulo" para utilizar a fonte "font"
        self.Titulo.setObjectName("Titulo")#nome do objeto

        #cemElementos
        self.cemElementos = QtWidgets.QPushButton(self.centralwidget)#definindo o Widget "cemElementos" como um botão
        self.cemElementos.setGeometry(QtCore.QRect(30, 60, 101, 23))#coordenadas(x,y) e tamanho(largura,altura) do botão "cemElementos"
        self.cemElementos.clicked.connect(self.cemElementos_clicked)#método definido quando o botão "cemElementos" for pressionado
        self.cemElementos.setObjectName("cemElementos")#nome do objeto

        #milElementos
        self.mil_elementos = QtWidgets.QPushButton(self.centralwidget)
        self.mil_elementos.setGeometry(QtCore.QRect(160, 60, 111, 23))
        self.mil_elementos.clicked.connect(self.milElementos_clicked)
        self.mil_elementos.setObjectName("mil_elementos")
        

        #dezMilElementos
        self.dezMilElementos = QtWidgets.QPushButton(self.centralwidget)
        self.dezMilElementos.setGeometry(QtCore.QRect(300, 60, 101, 23))
        self.dezMilElementos.clicked.connect(self.dezMilelementos_clicked)
        self.dezMilElementos.setObjectName("dezMilElementos")
        
        #Bubble
        self.Bubble = QtWidgets.QLabel(self.centralwidget)
        self.Bubble.setGeometry(QtCore.QRect(30, 130, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Bubble.setFont(font)
        self.Bubble.setObjectName("Bubble")
        
        #Selection
        self.Selection = QtWidgets.QLabel(self.centralwidget)
        self.Selection.setGeometry(QtCore.QRect(30, 160, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Selection.setFont(font)
        self.Selection.setObjectName("Selection")

        #Tempo_execucao
        self.Tempo_execucao = QtWidgets.QLabel(self.centralwidget)
        self.Tempo_execucao.setGeometry(QtCore.QRect(150, 100, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Tempo_execucao.setFont(font)
        self.Tempo_execucao.setObjectName("Tempo_execucao")

        #Insertion
        self.Insertion = QtWidgets.QLabel(self.centralwidget)
        self.Insertion.setGeometry(QtCore.QRect(30, 190, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.Insertion.setFont(font)
        self.Insertion.setObjectName("Insertion")

        #sort
        self.sort = QtWidgets.QLabel(self.centralwidget)
        self.sort.setGeometry(QtCore.QRect(30, 220, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.sort.setFont(font)
        self.sort.setObjectName("sort")

        #menubar e statusbar
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

    #caso o botao "cemElementos" seja clickado
    def cemElementos_clicked(self):

        self.Titulo.setText("100 elementos: ") #definindo o label "Titulo" para "100 elementos: "

        #definindo o n com valor 100 para funcionamento das funções responsáveis pelos organizadores
        n=100
        Listas(n)
        execucao_orcanizadores(Listas)

        #atualizando a mensagem mostrada pelos label's para assim mostrar o tempo de execução de cada organizador
        self.Bubble.setText(_translate("MainWindow", "Bubble: "+ tempo_bubble))
        self.Selection.setText(_translate("MainWindow", "Selection: "+ tempo_selection))
        self.Insertion.setText(_translate("MainWindow", "Insertion: "+ tempo_insertion))
        self.sort.setText(_translate("MainWindow", "Sort() :"+ tempo_sort))

        

    #caso o botão "milElementos" seja clickado
    def milElementos_clicked(self):

        self.Titulo.setText("1000 elementos: ")

        n= 1000
        Listas(n)
        execucao_orcanizadores(Listas)


        self.Bubble.setText(_translate("MainWindow", "Bubble: "+ tempo_bubble))
        self.Selection.setText(_translate("MainWindow", "Selection: "+ tempo_selection))
        self.Insertion.setText(_translate("MainWindow", "Insertion: "+ tempo_insertion))
        self.sort.setText(_translate("MainWindow", "Sort() :"+ tempo_sort))

        

    #caso o botão "dezMilElementos" seja clickado
    def dezMilelementos_clicked(self):

        self.Titulo.setText("10000 elementos: ")

        n= 10000
        Listas(n)
        execucao_orcanizadores(Listas)


        self.Bubble.setText(_translate("MainWindow", "Bubble: "+ tempo_bubble))
        self.Selection.setText(_translate("MainWindow", "Selection: "+ tempo_selection))
        self.Insertion.setText(_translate("MainWindow", "Insertion: "+ tempo_insertion))
        self.sort.setText(_translate("MainWindow", "Sort() :"+ tempo_sort))

    #definindo as mensagens mostradas pelos label's e botões em primeiro momento
    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(_translate("MainWindow", "Organizadores"))
        self.Titulo.setText(_translate("MainWindow", "Escolha o tamanho de sua lista:"))
        self.cemElementos.setText(_translate("MainWindow", "100 elementos"))
        self.mil_elementos.setText(_translate("MainWindow", "1000 elementos"))
        self.dezMilElementos.setText(_translate("MainWindow", "10000 elementos"))


    #main
if __name__ == "__main__":
   
    app = QtWidgets.QApplication(sys.argv)#define "app" como o cache
    MainWindow = QtWidgets.QMainWindow()#define a MainWindow com as funções criqadas anteriormente
    ui = Ui_MainWindow()#define "ui" como a janela criada
    ui.setupUi(MainWindow)#inicializa a UI
    MainWindow.show() #mostra a UI criada
    sys.exit(app.exec_())#finaliza o algorítmo caso o usuário clique no "X" para fechar a janela
