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

 
 #Como solo se debe regresar un print con un mensaje que diga lo que hace cada subprograma, no se le coloco ningun return. Pero si se coloco que tipo de
 #variable regresa a cada subprograma

def DeterminarPartidaTerminada (N:int, M:int, Ganador:int, Matrix:int, siguePartida:bool) -> bool:
	#Precondicion: N>0 and M>0 and (Ganador=0 or Ganador=1 or Ganador=2)
	#Postcondicion: siguePartida= True or siguePartida= False

 print("Este proceso determina si la partida termino")

def DeterminarGanador (N:int, M:int, turno: int, Matrix:int, Ganador:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: Ganador=0 or Ganador=1 or Ganador=2
 
 print("Este proceso determina el Ganador de la partida, usara los subprogramas LineaHorizontal, LineaVertical, LineaDiagonalIzquierda, LineaDiagonalDerecha")

def LineaVertical(N:int, M:int, turno:int, Matrix:int, Ganador:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: Ganador=0 or Ganador=1 or Ganador=2
 
 print("Este proceso recorre la matriz y verifica si hay una linea Vertical ganadora (Usada por Determinar Ganador)")


def LineaHorizontal(N:int, M:int, turno:int, Matrix:int, Ganador:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: Ganador=0 or Ganador=1 or Ganador=2
 
 print("Este proceso recorre la matriz y verifica si hay una linea Horizontal ganadora (Usada por Determinar Ganador)")

def LineaDiagonalDerecha(turno:int, Matrix:int, Ganador:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: Ganador=0 or Ganador=1 or Ganador=2
 
 print("Este proceso recorre la matriz y verifica si hay una linea Diagonal Derecha ganadora (Usada por Determinar Ganador)")

def LineaDiagonalIzquierda (turno:int, Matrix:int, Ganador:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: Ganador=0 or Ganador=1 or Ganador=2
 
 print("Este proceso recorre la matriz y verifica si hay una linea Diagonal Izquierda ganadora (Usada por Determinar Ganador)")
 
def SeguirJugando (siguePartida:bool) -> bool:
	#Precondicion: siguePartida=True
	#Postcondicion: siguePartida=True or siguePartida=False

 print("Este proceso determina si se desea seguir jugando o no (Se le pregunta al jugador luego de cada jugada)")
 siguePartida=False #Esto se le agrega para probar el flujo del programa y no quede dentro del bucle
 
 return siguePartida
 
def DesplegarGanador(Ganador:int) -> 'Void': 
	#Precondicion: Ganador=1 or Ganador=0 or Ganador=2
	#Postcondicion: True
 
 print("Este proceso Muestra en pantalla el ganador de la partida luego de que esta termine")
 
def otraPartida(jugarOtra:bool, PrimeraPartida:bool) -> bool:
	#Precondicion: jugarOtra=True
	#Postcondicion: jugarOtra=True or jugarOtra=False

 print("Este proceso Pregunta el jugador, luego de que termina una partida, si se desea jugar otra")
 jugarOtra=False #Esto se le agrega para probar el flujo del programa y no quede dentro del bucle

 return jugarOtra

def ReflejarJugada(i:int, jugada:int, turno:int, Matrix:int) -> 'Void':
	#Precondicion: turno=1 or turno=2
	#Postcondicion: True

 print("Refleja en pantalla la jugada hecha por el CPU y el jugador")

def CambiarTurno(turno:int) -> int:
	#Precondicion: turno=1 or turno=2
	#Postcondicion: turno=1 or turno=2

 print("Cambia el turno al otro jugador")

def validarJugada(N: int, M:int, Matrix:int, jugada:int, esValida:bool, i:int):
	#Precondicion: N>0 and M>0
	#Postcondicion: esValida=0 or esValida=1

 print("Este proceso determinara si la Jugada del jugador es valida y la colocara en la matriz")
 esValida=False #Esto se le agrega para probar el flujo del programa y no quede dentro del bucle

 return esValida

def InicializarPartida(Ganador:int, N:int, M:int,Linea:int , p:int, q:int,JugadaPrimeraVez:bool, nombreJugador:str ,Nivel:int, Matrix:int, turno:int):
	#Precondicion: N>0 and M>0
	#Postcondicion: (%forall i,j: 0<=i<N and 0<=j<M : Matrix[i][j]=0)
    
 print("Este proceso inicializara la partida, poniendo el tablero vacio, e inicializando todas las variables que se necesitara en el nuevo juego")

def ObtenerJugada(nivel:int, turno:int, nombreJugador:str, N:int, M:int, Matrix:int, JugadaPrimeraVez:bool, Linea:int, p:int, q:int, jugada:int):
	#Precondicion: N>0 and M>0 and (turno=1 or turno=2) and (nivel=1 or nivel=2)
	#Postcondicion: (%exist i: 0<=i<=5: Linea=i) and 0<=p<N and 0<=q<M and 0<=jugada<M

 print("Este proceso es donde el jugador y el CPU decidiran la jugada que quieren hacer. Si se selecciona el nivel medio, el CPU usa de otros subprogramas (mencionados abajo) para hacer su jugada y determinar si es valida")
 

def DeterminarLinea(N:int, M:int, Matrix:int, p:int, q:int, Linea:int) -> int:
	#Precondicion: (%exist i: 0<=i<=5: Linea=i)
	#Postcondicion: (%exist i: 0<=i<=5: Linea=i)

 print("Este proceso determinara la Linea que el CPU desea jugar cuando juegue en el nivel medio")


def DeterminarJugadaValida (N:int, M:int, Matrix:int, i:int, j:int, Valida:bool) -> bool:
	#Precondicion: N>0 and M>0
	#Postcondicion: Valida=False \/ Valida=True
 
 print("Este proceso es usado por DeterminarLinea para verificar si, al escoger una linea, puede colocar la ficha en ese espacio (Solo se usaria si el CPU se le asigna el nivel medio)")

def ResaltarLinea(a:int, b:int, c:int, d:int) -> 'Void':
	#Precondicion: (%forall i: i={a,b,c,d}: i=1 \/ i=2 )
	#Poscondicion: True
 
 print("Si se encuentra una Linea ganadora, la resalta (Usada por LineaHorizontal, LineaVertical, LineaDiagonalDerecha y LineaDiagonalIzquierda)")

def DesplegarResultadoFinal(Ganador0:int, Ganador1:int, Ganador2:int) -> 'Void':
	#Precondicion: ganador1>=0 and ganador2>=0 and ganador0>=0
	#Postcondicion: True

 print("Este proceso desplegara en pantalla la cantidad de veces que el jugador ha ganado, la cantidad de veces que gano el CPU y cuantas veces quedo en empate")

def ContarGanadorPartida(Ganador, Ganador0, Ganador1, Ganador2) -> int:
	#Precondicion: Ganador=0 or Ganador=1 or Ganador=2
	#Postcondicion: Ganador0>=0 and Ganador1>=0 and Ganador2>=0

 print("Cuenta cuantas veces ha quedado en empate, cuantas veces Gano el jugador y cuantas veces gano la computadora")

#Variables declaradas / Se les puso un valor cualquiera solo para declararlas, dentro del programa en Inicializar partida se les colocara sus verdaderos valores
N=6
M=7
nombreJugador="Nombre"
Tablero=[[0 for j in range(M)] for i in range(N)]
nivel=0
i=0
turno=0
JugadaPrimeraVez=True
Linea=5
jugada=0
Ganador=0
esValida=True
p=0
q=0


jugarOtra, PrimeraPartida=True,True
Ganador0, Ganador1, Ganador2=0,0,0
while jugarOtra==True:
	InicializarPartida(Ganador,N,M,Linea,p,q,JugadaPrimeraVez,nombreJugador,nivel,Tablero, turno) 
	siguePartida=True
	while siguePartida==True:                                                                                                                                                                      
		ObtenerJugada(nivel, turno, nombreJugador, N, M, Tablero, JugadaPrimeraVez, Linea, p, q, jugada) 
		esValida=validarJugada(N,M,Tablero,jugada,esValida,i)
		if esValida==True:            
			ReflejarJugada(i,jugada,turno,Tablero)            
			CambiarTurno(turno)       
		elif esValida==False:           
			pass
		DeterminarGanador(N,M,turno,Tablero,Ganador) 
		DeterminarPartidaTerminada(N,M,Ganador,Tablero,siguePartida) 
		siguePartida=SeguirJugando(siguePartida) 
	DesplegarGanador(Ganador) 
	ContarGanadorPartida(Ganador, Ganador0, Ganador1, Ganador2)
	jugarOtra=otraPartida(jugarOtra, PrimeraPartida)  
DesplegarResultadoFinal(Ganador0, Ganador1, Ganador2) 

