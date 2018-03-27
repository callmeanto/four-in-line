#
# Juego4enLineaEquipo04.py
#
# Descripcion: Este es el algoritmo que sigue el juego  Cuatro en linea, que consiste en una matriz 6x7 y dos "fichas" (para 2 jugadores) 
#              que tendran el valor 1 y 2 cuando ocupen una posicion en la Matriz, el objetivo del juego es completar una linea de 4 fichas 
#              de forma vertical, horizontal o Diagonal.
#
# Autores: Pietro Iaia
#          Antonella Requena
#
#    Ultima fecha de modificacion: 13/03/2018



#VARIABLES
# N: int // Esta contendra cuantas filas tiene la matriz (Para este programa, N sera 6)
# M: int // Esta contendra cuantas columnas tiene la matriz (Para este programa, M sera 7)
# NombreJugador: str // Este contendra el nombre del jugador
# Tablero: array [0..N)[0..M) of int // Esta variable sera usada para contener la matriz
# nivel: int // Esta contendra el nivel quje se desea jugar
# i: int // Guarda la ultima fila jugada por el usuario para luego verificar si es Valido jugar ahi
# turno: int // Variable que contendra el turno de los jugadores y cambia cada vez que pasa por el ciclo
# JugadaPrimeraVez: bool // Variable usada para ver si el CPU en el nivel medio ya jugo por primera vez
# Linea: int // Variable que contiene la Linea que el CPU desea jugar en el nivel medio
# jugada: int // Variable que contendra la ultima columna jugada por el jugador y el CPU en el nivel principiante
# Ganador: int // Variable que contiene el Ganador de la partida (Siempre sera 0 hasta que se decida si se queda asi o cambia a 1 o 2)
# esValida: bool // Variable para determinar si la jugada del jugador es Valida o no
# siguePartida: bool // Variable que determina si la partida sigue o ya termino
# jugarOtra: bool // Variable para determinar si se desea jugar otra partida o no
# p :int // Variable que contendra la ultima fila jugada por el CPU en el nivel medio
# q: int // Variable que contendra la ultima columna jugada por el CPU en el nivel medio
# Ganador0:int // Cuenta cuantas veces ha quedado en empate la partida
# Ganador1:int // Cuenta cuantas veces ha ganado el Jugador
# Ganador2:int // Cuenta cuantas veces ha ganado el computador
# PrimeraPartida: bool // Esta variable verifica si es la primera partida que se juega entre el computador y el jugador


#Imports
import os 
import sys
import pygame
import random


def DeterminarPartidaTerminada (N:int, M:int, Ganador:int, Matrix:int, siguePartida:bool) -> bool:
	#Precondicion: N>0 and M>0 and (Ganador=0 or Ganador=1 or Ganador=2)
	#Postcondicion: siguePartida= True or siguePartida= False
	n=0
	i=0
	while i<N:
		j=0
		while j<M:
			if Matrix[i][j]==0:
				n=1                                    #Este ciclo recorre la matriz y revisa si aun hay espacios en blanco(con 0)
			elif Matrix[i][j]!=0:                      #Si hay, n=1, si no, no hace nada
				pass
			j=j+1
		i=i+1
	if n==1:
		pass                                           #Si n==1, no pasa nada, si n!=1 (es decir, no se encontraron espacios en blanco)
	elif n!=1:                                         #La partida termina (siguePartida=False)
		siguePartida=False

	if Ganador==0:
		pass
	elif Ganador==1:                                   #Aqui es donde ve si termina la partida si algun ganador hace un 4 en linea
		siguePartida=False                             #Si queda en empate, entra en Ganador==0 y no hace nada ya que ya puso siguePartida=False arriba
	elif Ganador==2:                                   #Si cae en Ganador==1 o Ganador==2, termina la partida ya que gano el computador o el jugador
		siguePartida=False
	return siguePartida


def DeterminarGanador (N:int, M:int, turno: int, Matrix:int, Ganador:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: Ganador=0 or Ganador=1 or Ganador=2

	Ganador=LineaVertical (N, M, turno, Matrix, Ganador)
	Ganador=LineaHorizontal (N, M, turno, Matrix, Ganador)            #Aqui llama a cada proceso que verifica las lineas dependiendo de su sentido
	Ganador=LineaDiagonalIzquierda (turno, Matrix, Ganador)           
	Ganador=LineaDiagonalDerecha (turno, Matrix, Ganador)
	return Ganador


def LineaVertical(N:int, M:int, turno:int, Matrix:int, Ganador:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: Ganador=0 or Ganador=1 or Ganador=2
	i=0
	while(i<N-3):
		j=0
		while j<M:
			if Matrix[i][j]==turno and Matrix[i+1][j]==turno and Matrix[i+2][j]==turno and Matrix[i+3][j]==turno:
				Ganador=turno
			else:                                       #Se verifica si hay 4 en linea vertical, si lo hay, asigna Ganador=1 o Ganador=2
				pass                                    #Dependiendo de quien haya hecho la ultima jugada (turno)
			j=j+1
		i=i+1
	return Ganador
 

def LineaHorizontal(N:int, M:int, turno:int, Matrix:int, Ganador:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: Ganador=0 or Ganador=1 or Ganador=2
	j=0
	while j<M-3:
		i=0
		while i<N:
			if Matrix[i][j]==turno and Matrix[i][j+1]==turno and Matrix[i][j+2]==turno and Matrix[i][j+3]==turno:
				Ganador=turno
			else:                                     #Se verifica si hay 4 en linea horizontal, si lo hay, asigna Ganador=1 o Ganador=2
				pass                                  #Dependiendo de quien haya hecho la ultima jugada (turno)
			i=i+1
		j=j+1
	return Ganador
 

def LineaDiagonalDerecha(turno:int, Matrix:int, Ganador:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: Ganador=0 or Ganador=1 or Ganador=2
	i=0
	while i<3:
		j=0
		while j<4:
			if Matrix[i][j]==turno and Matrix[i+1][j+1]==turno and Matrix[i+2][j+2]==turno and Matrix[i+3][j+3]==turno:
				Ganador=turno
			else:                                   #Se verifica si hay 4 en linea Diagonal Derecha, si lo hay, asigna Ganador=1 o Ganador=2
				pass                                #Dependiendo de quien haya hecho la ultima jugada (turno)
			j=j+1
		i=i+1
	return Ganador
 

def LineaDiagonalIzquierda (turno:int, Matrix:int, Ganador:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: Ganador=0 or Ganador=1 or Ganador=2
	i=0
	while i<3:
		j=6
		while j>2:
			if Matrix[i][j]==turno and Matrix[i+1][j-1]==turno and Matrix[i+2][j-2]==turno and Matrix[i+3][j-3]==turno:
				Ganador=turno
			else:                                 #Se verifica si hay 4 en linea Diagonal Izquierda, si lo hay, asigna Ganador=1 o Ganador=2
				pass                              #Dependiendo de quien haya hecho la ultima jugada (turno)
			j=j-1
		i=i+1
	return Ganador

 
def SeguirJugando (siguePartida:bool) -> bool:
	#Precondicion: siguePartida=True
	#Postcondicion: siguePartida=True or siguePartida=False

 print("Este proceso determina si se desea seguir jugando o no (Se le pregunta al jugador luego de cada jugada)")
 siguePartida=False #Esto se le agrega para probar el flujo del programa y no quede dentro del bucle
 
 return siguePartida
 
def DesplegarGanador(Ganador:int) -> 'Void': 
	#Precondicion: Ganador=1 or Ganador=0 or Ganador=2
	#Postcondicion: True

	if Ganador==1:
		print("El ganador de la partida es " +NombreJugador+ "!")
	elif Ganador==2:
		print("El ganador de la partida es el computador!")
	elif Ganador==0:
		print("La partida termino en empate!")

 
 
def otraPartida() -> bool:
	#Precondicion: jugarOtra=True
	#Postcondicion: jugarOtra=True or jugarOtra=False	

	PrimeraPartida=False                               #Se le asigna PrimeraPartida=False ya que termino la primera partida entre el jugador y
	print("La partida ha finalizado")                  #la Computadora
	print("¿Desea jugar otra partida?")	

	while True:
		y=str(input("Si o no?"))
		if y=="Si":
			jugarOtra=True                              #Pide al usuario si desea jugar otra vez, si escribe algo diferente a Si o No
			break                                       #Se le avisara que solo puede escoger entre Si o No
		elif y=="No":
			jugarOtra=False
			break
		else:
			print("Solo se puede escoger entre Si o No")
			continue
	return PrimeraPartida, jugarOtra
		

def ReflejarJugada(i:int, jugada:int, turno:int, Matrix:int) -> 'Void':
	#Precondicion: turno=1 or turno=2
	#Postcondicion: True

 print("Refleja en pantalla la jugada hecha por el CPU y el jugador")

def CambiarTurno(turno:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: turno=1 or turno=2
	if turno==2:
		turno=1                                          #Aqui cambia el turno, si entra con turno==1, lo cambia a turno=2 y viceversa
	else:
		turno=2
	return turno


def validarJugada(N: int, M:int, Matrix:int, jugada:int, esValida:bool, i:int):
	#Precondicion: N>0 and M>0
	#Postcondicion: esValida=0 or esValida=1

 print("Este proceso determinara si la Jugada del jugador es valida y la colocara en la matriz")
 esValida=False #Esto se le agrega para probar el flujo del programa y no quede dentro del bucle

 return esValida

def InicializarPartida(PrimeraPartida:bool, Ganador:int, N:int, M:int) -> (str,int,bool):
	#Precondicion: N>0 and M>0
	#Postcondicion: (%forall i,j: 0<=i<N and 0<=j<M : Matrix[i][j]=0)

	#ENTRADA DE DATOS
	nombreJugador=str(input("Ingrese su nombre: "))
	print("Indique  el nivel que desea jugar")
	print("Nivel Básico: Tipee 1.")                                 #Aqui se le pide al usuario ingresar su nombre y un nivel
	print("Nivel Medio: Tipee 2.")                                  #Si tipea algo mas que 1 o 2 en nivel, se le avisara que solo
	while True:                                                     #puede tipear Nivel 1 o Nivel 2
		nivel=int(input("Nivel:"))
		if nivel==1:
			break
		elif nivel==2:
			break
		else:
			print("Solo puede ingresar Nivel 1 o Nivel 2")
			continue

	#INICIALIZACION DEL TABLERO
	Matrix=[[0 for x in range(M)] for x in range(N)]             #Pone todas las casillas en 0 para iniciar la partida
    
	#Variables para el nivel medio del CPU
	Linea=5                                            #Linea=5 ya que se necesitara mas adelante en el codigo que sea asi
	q,p= random.randint(0,6),5                         #p y q son las jugadas de la computadora en el nivel medio. Estas variables son para guardar su ultima jugada.
	JugadaPrimeraVez=True                              #JugadaPrimeraVez=True ya que seria la primera vez que juega la computadora en esta partida

	#Turnos
	if PrimeraPartida==True:
		turno=2
	elif PrimeraPartida==False:                        #Si es la Primera Partida de la sesion, se le asigna el turno a la computadora
		if Ganador==1:                                 #Si no, se verifica quien es el ganador de la partida pasada y empezaria el
			turno=1                                    #Y si quedo empatado, empieza la computadora
		elif Ganador==2 or Ganador=0:
			turno=2
	
	return nombreJugador, nivel, Matrix, Linea, q, p, JugadaPrimeraVez, turno


def ObtenerJugada(nivel:int, turno:int, nombreJugador:str, N:int, M:int, Matrix:int, JugadaPrimeraVez:bool, Linea:int, p:int, q:int, jugada:int):
	#Precondicion: N>0 and M>0 and (turno=1 or turno=2) and (nivel=1 or nivel=2)
	#Postcondicion: (%exist i: 0<=i<=5: Linea=i) and 0<=p<N and 0<=q<M and 0<=jugada<M

 print("Este proceso es donde el jugador y el CPU decidiran la jugada que quieren hacer. Si se selecciona el nivel medio, el CPU usa de otros subprogramas (mencionados abajo) para hacer su jugada y determinar si es valida")
 

def DeterminarLinea(N:int, M:int, Matrix:int, p:int, q:int, Linea:int) -> int:
	#Precondicion: (%exist i: 0<=i<=5: Linea=i)
	#Postcondicion: (%exist i: 0<=i<=5: Linea=i)

	#VAR Valida0, Valida1, Valida2, Valida3, Valida4, SigueFila :bool  

	Valida0=DeterminarJugadaValida(N, M, Matrix, p, q+1)  
	Valida1=DeterminarJugadaValida(N, M, Matrix, p, q-1)  
	Valida2=DeterminarJugadaValida(N, M, Matrix, p-1, q)           #En estos procesos se verfica si cada posible fila tiene ficha abajo.
	Valida3=DeterminarJugadaValida(N, M, Matrix, p-1, q+1) 
	Valida4=DeterminarJugadaValida(N, M, Matrix, p-1, q-1) 
	SigueFila=False                                                #Se le asigna SigueFila=False para declararla, puede que su valor cambie en el if de abajo

	if Linea==0:
		sigueFila=DeterminarJugadaValida (N, M, Matrix, p, q+1)
	elif Linea==1:
		sigueFila=DeterminarJugadaValida (N, M, Matrix, p, q-1) 
	elif Linea==2:
		sigueFila=DeterminarJugadaValida (N, M, Matrix, p-1, q)       #Aqui verifica si puede seguir jugando en la Linea en que esta, si no 
	elif Linea==3:                                                    #SigueFila=False y se le determina una nueva Fila
		sigueFila=DeterminarJugadaValida (N, M, Matrix, p-1, q+1)
	elif Linea==4:
		sigueFila=DeterminarJugadaValida (N, M, Matrix, p-1, q-1)
	elif Linea==5:
		pass


	if SigueFila==True:
		pass
	elif SigueFila==False:                               #Si al determinar que puede seguir en la misma fila SigueFila==True, entonces
		if Valida0==True:                                #No hay necesidad de cambiarle la Linea y hacemos pass
			Linea=0                                      #Pero si SigueFila==False es porque no puede seguir en esa Linea y se verifica en cual direccion
		elif Valida1==True:                              #desea empezar a construir y al encontrar una se le asigna la Linea correspondiente
			Linea=1                                      #Si no puede construir para ninguna direccion desde donde esta, se le asigna Linea=5
		elif Valida2==True:
			Linea=2
		elif Valida3==True:
			Linea=3
		elif Valida4==True:
			Linea=4
		else:                               
			Linea=5

	return Linea



def DeterminarJugadaValida (N:int, M:int, Matrix:int, i:int, j:int) -> bool:
	#Precondicion: N>0 and M>0
	#Postcondicion: Valida=False \/ Valida=True

	if i>=0 and i<=N-1 and j>=0 and j<=M-1:
		if Matrix[i][j]==0:
			if i=5:
				Valida=True
			elif i!=5: 
				if Matrix[i+1][j]==1 or Matrix[i+1][j]==2: 
					Valida= True
				elif Matrix[i+1][j]==0:
					Valida=False
		elif Matrix[i][j]!=0:
			Valida=False
	elif i<0 or i>N-1 or j<0 or j>M-1:
		Valida=False

	return Valida
 


def ResaltarLinea(a:int, b:int, c:int, d:int) -> 'Void':
	#Precondicion: (%forall i: i={a,b,c,d}: i=1 \/ i=2 )
	#Poscondicion: True
 
 print("Si se encuentra una Linea ganadora, la resalta (Usada por LineaHorizontal, LineaVertical, LineaDiagonalDerecha y LineaDiagonalIzquierda)")

def DesplegarResultadoFinal(Ganador0:int, Ganador1:int, Ganador2:int) -> 'Void':
	#Precondicion: ganador1>=0 and ganador2>=0 and ganador0>=0
	#Postcondicion: True

	print("El resultado final es:")
	print("Total partidas ganadas por "+str(nombreJugador))
	print(Ganador1)
	print("Total partidas ganadas por la computadora ")
	print(Ganador2)
	print("Total partidas empatadas")
	print(Ganador0)


def ContarGanadorPartida(Ganador, Ganador0, Ganador1, Ganador2) -> int:
	#Precondicion: Ganador=0 or Ganador=1 or Ganador=2
	#Postcondicion: Ganador0>=0 and Ganador1>=0 and Ganador2>=0

	if Ganador==0:
		Ganador0=Ganador0+1
	elif Ganador==1:
    	Ganador1=Ganador1+1
 	elif Ganador=2:
		Ganador2==Ganador2+1

	return Ganador0, Ganador1, Ganador2




#Variables declaradas, mas adelante en el codigo se usaran
N=6
M=7
i=0
jugada=0
Ganador=0
esValida=True
jugarOtra, PrimeraPartida=True,True
Ganador0, Ganador1, Ganador2=0,0,0

while jugarOtra==True:
	nombreJugador, nivel, Tablero, Linea, q, p, JugadaPrimeraVez, turno = InicializarPartida(PrimeraPartida, Ganador, N, M) 
	siguePartida=True
	while siguePartida==True:                                                                                                                                                                      
		ObtenerJugada(nivel, turno, nombreJugador, N, M, Tablero, JugadaPrimeraVez, Linea, p, q, jugada) 
		esValida=validarJugada(N,M,Tablero,jugada,esValida,i)
		if esValida==True:            
			ReflejarJugada(i,jugada,turno,Tablero)            
			turno = CambiarTurno(turno)       
		elif esValida==False:           
			pass
		Ganador = DeterminarGanador(N,M,turno,Tablero, Ganador) 
		siguePartida = DeterminarPartidaTerminada(N, M, Ganador, Tablero, siguePartida) 
		siguePartida = SeguirJugando(siguePartida) 
	DesplegarGanador(Ganador) 
	Ganador0, Ganador1, Ganador2 = ContarGanadorPartida(Ganador, Ganador0, Ganador1, Ganador2)
	PrimeraPartida, jugarOtra = otraPartida()  
DesplegarResultadoFinal(Ganador0, Ganador1, Ganador2) 

