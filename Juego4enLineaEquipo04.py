# Juego4enLineaEquipo04.py
#
# Descripción: Este es el algoritmo que sigue el juego  Cuatro en linea, que consiste en una matriz 6x7 y dos "fichas" (para 2 jugadores) 
#              que tendran el valor 1 y 2 cuando ocupen una posicion en la Matriz, el objetivo del juego es completar una linea de 4 fichas 
#              de forma vertical, horizontal o Diagonal.
#
# Autores: Pietro Iaia
#          Antonella Requena
#
# Última fecha de modificación: 04/04/2018


# Librerías a importar
import os       # Se importa esta librería para 
import sys      # Se importa esta librería para utilizar sys.exit (versión robusta)
import pygame   # Se importa esta librería para la interfaz gráfica
import random   # Se importa esta librería para la implementación de la jugada del computador
import time     # Se importa esta librería para utilizar time.sleep para que se espere un tiempo antes de la siguiente jugada

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                 PROCEDIMIENTOS Y FUNCIONES                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# FUNCION PARA DETERMINAR SI LA PARTIDA TERMINO
def DeterminarPartidaTerminada(N:int, M:int, Ganador:int, Matrix:[int], siguePartida:bool) -> bool:
	# DESCRIPCIÓN:
	""" Este procedimiento es para determinar si la partida ya se termino mediante un return del booleano siguePartida. 
	    Recibe como parámetros N y M que son el tamaño de la matriz, recibe el entero Ganador que está entre 0 y 2 e indica
	    quien es el ganador para este punto de la partida, recibe la Matrix (el tablero) con el estado actual del juego, y el
	    booleano siguePartida, siempre lo recibe como True. Esta es la misma variable de salida, retorna siguePartida y puede valer
	    true o false dependiendo de lo siguiente:
	    Una partida se termina (siguePartida es True) si pasa alguna de las tres cosas:
	    1. La primera es si el tablero ya esta lleno, puesto que no hay mas espacio para jugar fichas, a nivel de codigo 
	    esto es recorriendo el arreglo (tablero) y chequeando si hay alguna casilla donde haya un 0 todavia, si lo hay, se le asigna 1
	    a una variable auxiliar, sino, se hace un pass. Al final del ciclo, se chequea, si n resulta ser 1, a siguePartida 
	    (parametro de entrada) se le asigna True dado que la partida aun puede continuar.
	    2. Si hay algun ganador. Si Ganador (parametro que recibe de entrada) es igual a 0, significa que aun no hay ganador, y si siguePartida
	    es False por el caso anterior, quiere decir que hay empate, si es true es porque aun se puede seguir jugando. Si Ganador es igual a 1,
	    a siguePartida se le asigna False puesto que ya gano el jugador. Análogo para Ganador igual a 2. 
	    3. Si el usuario no quiere seguir jugando, esto se verifica en otro procedimiento
	"""
	# Precondición: 
	assert(N>0 and M>0 and 0<=Ganador<=2 and siguePartida==True)
	
	n=0 # Variable auxiliar para saber si hay alguna casilla vacia
	i=0 # Variable de iteracion para recorrer filas del arreglo
	
    # CASO 1.
	while i<N:
		j=0  # Variable de iteracion para recorrer columnas del arreglo
		while j<M:
			if Matrix[i][j]==0:
				n=1                                    #Este ciclo recorre la matriz y revisa si aun hay casillas vacias (con 0)
			elif Matrix[i][j]!=0:                      #Si hay, n=1, si no, no hace nada
				pass
			j=j+1
		i=i+1
	if n==1:
		pass                                           #Si n==1, no pasa nada, siguePartida sigue siendo true
	elif n!=1:                                         #Si n!=1 (no hay espacios vacios), la partida termina (siguePartida=False)                                    
		siguePartida=False

    # CASO 2.
	if Ganador==0:
		pass
	elif Ganador==1:                                   #Aqui es donde ve si termina la partida si algun ganador hace un 4 en linea
		siguePartida=False                             #Si queda en empate, entra en Ganador==0 y no hace nada ya que ya puso siguePartida=False arriba
	elif Ganador==2:                                   #Si cae en Ganador==1 o Ganador==2, termina la partida ya que gano el computador o el jugador
		siguePartida=False
    
    # Postcondición: 
	assert((n==1 and siguePartida==True) or (n!=1 and siguePartida==False) or (1<=Ganador<=2 and siguePartida==False))

	return siguePartida


# FUNCION PARA DETERMINAR EL GANADOR DE LA PARTIDA
def DeterminarGanador(N:int, M:int, turno: int, Matrix:[int], Ganador:int) -> int:
	# DESCRIPCIÓN:
	""" Esta funcion es para determinar si hay algun ganador en la partida. Recibe como parametros N y M (tamaños del arreglo), 
	   el turno (en realidad es dado que el jugador se representa mediante el turno, es decir, si una linea se construye en 
	   el turno=1, quiere decir que quien la construyo fue el jugador 1, i.e el usuario), una matriz Matriz (el tablero)
	   y el ganador (que lo debe recibir como 0 siempre). La funcion debe retornar Ganador que en este caso puede ser 0 si ninguno
	   construyo alguna linea (No se cumple ninguna de las guardias de la seleccion), 
	   1 si la construyo el turno 1 o 2 si la construyo el turno 2.   

	   Las lineas candidatas a ganadoras pueden ser: Vertical, Horizontal, Diagonal Izquierda y Diagonal Derecha.
	   Lo que se verifica en cada "linea" es que se recorre la matriz buscando alguna fila o columna (dependiendo del tipo de linea)
	   donde las 4 casillas tengan el valor del turno (es decir, por ejemplo, si la verificacion es de linea horizontal, la columna queda
	   fija y lo que se verifica es si el valor de la casilla i y la i+1, i+2 e i+3 son iguales al turno actual, si es asi, el ganador sera
	   el del turno, sino, no se hace nada y ganador seguira siendo 0) 
	"""
	# Precondicion: 
	assert(1<=turno<=2 and N>0 and M>0 and Ganador==0)

    # LINEA VERTICAL
	i=0
	while(i<N-3):
		j=0
		while j<M:
			if Matrix[i][j]==turno and Matrix[i+1][j]==turno and Matrix[i+2][j]==turno and Matrix[i+3][j]==turno:
				Ganador=turno                           #Lo que hace es ver si en la fila i, i+1, i+2 e i+3 (las 3 consecutivas) 
				ResaltarLinea(j,i,j,i+1,j,i+2,j,i+3)    #(j es fijo) el valor de las casillas es 1 o 2.
			else:                                       #Si es asi, se asigna a Ganador=1 o Ganador=2 (dependiendo de quien sea el turno)
				pass                                    # y se resalta la linea. Sino, se hace un pass y Ganador sigue valiendo 0
			j=j+1
		i=i+1
 
    # LINEA HORIZONTAL
	j=0
	while j<M-3:
		i=0
		while i<N:
			if Matrix[i][j]==turno and Matrix[i][j+1]==turno and Matrix[i][j+2]==turno and Matrix[i][j+3]==turno:
				Ganador=turno
				ResaltarLinea(j,i,j+1,i,j+2,i,j+3,i)
			else:                                     #Se verifica si hay 4 en linea horizontal, si lo hay, asigna Ganador=1 o Ganador=2
				pass                                  #Dependiendo de quien haya hecho la ultima jugada (turno) y se resalta la linea
			i=i+1
		j=j+1

    # LINEA DIAGONAL DERECHA
	i=0
	while i<3:                                        #Se colocan estos valores para aseverar que no se salga del arreglo
		j=0
		while j<4:
			if Matrix[i][j]==turno and Matrix[i+1][j+1]==turno and Matrix[i+2][j+2]==turno and Matrix[i+3][j+3]==turno:
				Ganador=turno                         #Aqui tanto i como j crecen porque se esta aumentando de filas y columnas
				ResaltarLinea(j,i,j+1,i+1,j+2,i+2,j+3,i+3)
			else:                                     #Se verifica si hay 4 en linea Diagonal Derecha, si lo hay, asigna Ganador=1 o Ganador=2
				pass                                  #Dependiendo de quien haya hecho la ultima jugada (turno) y se resalta la linea
			j=j+1
		i=i+1
    
    # LINEA DIAGONAL IZQUIERDA
	i=0
	while i<3:
		j=6                                           #Se colocan estos valores para aseverar que no se salga del arreglo
		while j>2:
			if Matrix[i][j]==turno and Matrix[i+1][j-1]==turno and Matrix[i+2][j-2]==turno and Matrix[i+3][j-3]==turno:
				Ganador=turno                         #Aqui se aumenta se mueve de derecha a izquierda por lo que j disminuye, pero va subiendo
				ResaltarLinea(j,i,j-1,i+1,j-2,i+2,j-3,i+3)  #Por lo que i aumenta
			else:                                     #Se verifica si hay 4 en linea Diagonal Izquierda, si lo hay, asigna Ganador=1 o Ganador=2
				pass                                  #Dependiendo de quien haya hecho la ultima jugada (turno)
			j=j-1
		i=i+1
	# Todos estos ciclos no son excluyentes puesto que el jugador puede construir lineas simultaneas, 
    # por ejemplo, una diagonal y a su vez una vertical, y en dicho caso ambas se deben resaltar

    # Postcondicion:
	assert(0<=Ganador<=2)

	return Ganador

 # PROCEDIMIENTO PARA SALIR DEL JUEGO
def QuitGame(Ganador0:int, Ganador1:int, Ganador2:int, Matrix:[int]) -> 'void': 
    # DESCRIPCIÓN:
	""" Este procedimiento es para salir del juego cuando se intenta cerrar mediante la inferfaz, y se le pregunta al usuario
	si desea guardar su partida antes de salir. Los parametros de entrada son para almacenar las partidas ganadas por cada jugador 
	y la cantidad de empates, ademas del tablero. 
	"""
	
	print("¿Desea guardar su partida? [y/n]")
	while True:
		Respuesta=str(input("y o n "+'\n'))
		try:
			assert(Respuesta=='y' or Respuesta=='n')
			break
		except:
			print("Solo se puede ingresar 'y' si quiere o 'n' sino")  #Si se escribe algo mas que 'y' o 'n' informa que solo puede escoger entre esos dos
	if Respuesta=="y":
				f=open('save.txt','w')
				f.write(str(Ganador0)+'\n')
				f.write(str(Ganador1)+'\n')                #Se abre el 'save.txt' y se escribe los resultados totales en cada fila
				f.write(str(Ganador2)+'\n')
				f.close()
				pygame.quit()
				sys.exit()	
	elif Respuesta=="n":
				pygame.quit()                              #Se cierra el juego y no se guarda nada si se selecciona 'n'
				sys.exit()


# PROCEDIMIENTO PARA MOSTRAR EL GANADOR 
def DesplegarGanador(nombreJugador:str ,Ganador:int) -> 'void': 
    #Descripcion: Este procedimiento muestra en consola el ganador de la partida

	#Precondicion: 
	assert(0<=Ganador<=2)

	if Ganador==1:
		print("¡Enhorabuena! El ganador de la partida es " +nombreJugador+ "!")
	elif Ganador==2:
		print("El ganador de la partida es el computador!")
	elif Ganador==0:
		print("La partida terminó en empate!")
    #Postcondicion: No hay

 
# FUNCION PARA SABER SI EL JUGADOR QUIERE JUGAR OTRA PARTIDA
def otraPartida(Ganador0:int,Ganador1:int,Ganador2:int) -> (bool,bool):
    #Descripcion: Las variables de entrada son los contadores de cada ganador por partida, se reciben
    #             para poder ser almacenados en el archivo. Retorna 2 booleanos que dicen si es la primera
    #             partida y si el usuario quiere seguir jugando otra partida

	#Precondicion:
	assert(True)	

	PrimeraPartida=False                               #Se le asigna PrimeraPartida=False ya que termino la primera partida entre el jugador y
	print("La partida ha finalizado")                  #la Computadora
	print("¿Desea jugar otra partida?")	

	while True:
		y=str(input("Si o No?"+'\n'))
		if y=="Si":
			jugarOtra=True                              #Si se escoge Si, empieza el ciclo denuevo, si se escoge que No se le pedira si desea
			break                                       #Guardar la partida
		elif y=="No": 
			print("¿Desea Guardar su partida?")
			while True:
				Respuesta=str(input("Si o No?"+'\n'))
				if Respuesta=="Si":
					f=open('save.txt','w')
					f.write(str(Ganador0)+'\n')
					f.write(str(Ganador1)+'\n')                #Si se escoge Si, se abre el 'save.txt' y se escribe los resultados totales en cada fila
					f.write(str(Ganador2)+'\n')
					f.close()
					break	
				elif Respuesta=="No":                     
					break                                     
				else:
					print("Solo se puede ingresar Si o No")       #Si se escribe algo mas que 'Si' o 'No' le avisa que solo puede escoger entre esos dos
					continue
			jugarOtra=False                            #Se le asigna False a la variable y en el algoritmo principal sale del ciclo de jugar partida
			break                                      #Hace break para salir del ciclo
		else:
			print("Solo se puede escoger entre Si o No")                 #Pide al usuario si desea jugar otra vez, si escribe algo diferente a Si o No
			continue                                                     #Se le avisara que solo puede escoger entre Si o No

	#Postcondicion
	assert((jugarOtra==True and y=='Si') or (jugarOtra==False and y=='No'))

	return PrimeraPartida, jugarOtra
		
# FUNCION PARA CAMBIAR DE TURNO
def CambiarTurno(turno:int) -> int:
	#Descripcion: Este procedimiento cambia el turno, si es 1 lo cambia por 2 y viceversa

	#Precondicion:
	assert(1<=turno<=2)

	if turno==2:
		turno=1                                    #Aqui cambia el turno, si entra con turno==1, lo cambia a turno=2 y viceversa
	else:
		turno=2
	#Postcondicion
	assert(1<=turno<=2)

	return turno

# PROCEDIMIENTO PARA INICIALIZAR LA PARTIDA
def InicializarPartida(pantalla:int, PrimeraPartida:bool, Ganador:int, N:int, M:int) -> (str,int,bool):
	""" Descripcion: Este procedimiento inicializa el tablero, recibe como parametros 
	"""
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
	pantalla.fill(NEGRO)
	pygame.display.flip()
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
			Ganador=0                                  
		elif Ganador==2 or Ganador==0:                 #Se le pone Ganador=0 ya que al iniciar la partida otra vez, se debe reiniciar esa variable
			turno=2
			Ganador=0
	
	return Ganador, nombreJugador, nivel, Matrix, Linea, q, p, JugadaPrimeraVez, turno

# FUNCION PARA VALIDAR LA JUGADA DEL USUARIO
def ValidarJugada(Matrix:[int], Columna:int) -> bool:
	# Descripcion: Recibe la matriz del tablero y la columna que quiere jugar el usuario
	# chequea si la fila de dicha columna no esta llena

	#Precondicion
	assert(0<=Columna<=6)

	Fila=5
	while Fila>=0 and Matrix[Fila][Columna]!=0:
		Fila=Fila-1                              #Revisa Fila por fila en la columna que jugo el usuario hasta que encuentre una vacia
                                                 #Si Fila==-1 es porque recorrio toda la fila (de la posicion 5 a la 0) 
							                     #y no encontro alguna casilla con 0
    #Postcondicion
	assert((Fila==-1 and all(Matrix[Fila][Columna]!=0 for Fila in range(6)) ) or (0<=Fila<=5 and any(Matrix[Fila][Columna]==0 for Fila in range(6))))

    # Salida 
	return Fila

# FUNCION PARA OBTENER LA JUGADA TANTO DEL USUARIO COMO DEL COMPUTADOR
def ObtenerJugada(JugadaColumnaJugador:int, nivel:int, turno:int, nombreJugador:str, N:int, M:int, Matrix:[int], JugadaPrimeraVez:bool, Linea:int, p:int, q:int, Ganador0:int, Ganador1:int, Ganador2:int) -> 'void':
	""" Descripcion: 
        Este procedimiento recibe como parametros JugadaColumnaJugador que es la jugada del usuario, el nivel que es 1 o 2 para saber
        que estrategia seguira el computador, el turno para saber si pedira la entrada de la jugada del usuario o si jugara el computador
        el nombre del jugador para indicarle que es su turno y preguntarle si desea seguir jugando, N y M tamaños de la matriz, Matrix es e
        el tablero, JugadaPrimeraVez un bool que se le asigna True si es la primera jugada de la partida, Linea que es la fila en la que juega el
        computador, p y q corresponden a la fila p-esima y la columna q-esima y representan la casilla de la ultima jugada del computador.
        Ganador0, Ganador1 y Ganador2 representan los contadores de los ganadores por partida (0 es empate, 1 es usuario y 2 es CPU)
	"""
	#Precondicion: 
	assert(N>0 and M>0 and (turno==1 or turno==2) and (nivel==1 or nivel==2))

	#Coordenadas de circulos
	ColumnaCirculo=[205,346,486,627,768,909,1050]        #Estas son las coordenadas de los circulos en el tablero
	FilaCirculo=[135,220,310,395,485,575]

	#Lineas De seleccion:
	Linea0Ini=(130,50)
	Linea0Fin=(271,50)
	Linea1Ini=(271,50)
	Linea1Fin=(412,50)
	Linea2Ini=(412,50)                        #Estas son las coordenadas de la Linea blanca que sirve para seleccionar la jugada
	Linea2Fin=(553,50)
	Linea3Ini=(553,50)
	Linea3Fin=(694,50)
	Linea4Ini=(694,50)
	Linea4Fin=(835,50)
	Linea5Ini=(835,50)
	Linea5Fin=(976,50)
	Linea6Ini=(976,50)
	Linea6Fin=(1117,50)

	while True:
        # Hacer que el juego corrar a una velocidad que deseemos
		reloj.tick(FPS)
		# TURNO DEL USUARIO
		if turno==1:
			for evento in pygame.event.get():
            	# Si el evento que esta ocurriendo es que se acabo el juego, entonces cerrarlo
				if evento.type == pygame.QUIT:
					QuitGame(Ganador0, Ganador1, Ganador2,Matrix)
            		# Dibujar una Linea cuando se presiona el mouse, y borra la anterior dibujada
				# SI EL EVENTO ES MOVERSE ENTRE COLUMNAS
				elif evento.type == pygame.MOUSEBUTTONDOWN:
					if JugadaColumnaJugador==6:
						JugadaColumnaJugador=0
					else:                                                 #Cada vez que se oprima el mouse, cambia de Columna, cuando llegue a la 6, se devuelve
						JugadaColumnaJugador=JugadaColumnaJugador+1       #a la 0
                    
					if JugadaColumnaJugador==0:
						pygame.draw.line(pantalla, NEGRO, Linea6Ini, Linea6Fin, 7)
						pygame.draw.line(pantalla, BLANCO, Linea0Ini, Linea0Fin, 7)
					elif JugadaColumnaJugador==1:
						pygame.draw.line(pantalla, NEGRO, Linea0Ini, Linea0Fin, 7)
						pygame.draw.line(pantalla, BLANCO, Linea1Ini, Linea1Fin, 7)
					elif JugadaColumnaJugador==2:
						pygame.draw.line(pantalla, NEGRO, Linea1Ini, Linea1Fin, 7)
						pygame.draw.line(pantalla, BLANCO, Linea2Ini, Linea2Fin, 7)      #Aqui se dibuja la linea y se borra la linea anteriormente creada
					elif JugadaColumnaJugador==3:
						pygame.draw.line(pantalla, NEGRO, Linea2Ini, Linea2Fin, 7)
						pygame.draw.line(pantalla, BLANCO, Linea3Ini, Linea3Fin, 7)
					elif JugadaColumnaJugador==4:
						pygame.draw.line(pantalla, NEGRO, Linea3Ini, Linea3Fin, 7)
						pygame.draw.line(pantalla, BLANCO, Linea4Ini, Linea4Fin, 7)
					elif JugadaColumnaJugador==5:
						pygame.draw.line(pantalla, NEGRO, Linea4Ini, Linea4Fin, 7)
						pygame.draw.line(pantalla, BLANCO, Linea5Ini, Linea5Fin, 7)
					elif JugadaColumnaJugador==6:
						pygame.draw.line(pantalla, NEGRO, Linea5Ini, Linea5Fin, 7)
						pygame.draw.line(pantalla, BLANCO, Linea6Ini, Linea6Fin, 7)
            	#Dibuja un circulo dependiendo de donde este la posicion de la Linea

            	# SI EL EVENTO ES SELECCIONAR LA COLUMNA (HACER JUGADA)
				elif evento.type == pygame.KEYDOWN:
					if evento.key == pygame.K_SPACE:
						Fila=ValidarJugada(Matrix,JugadaColumnaJugador)
						if Fila==-1:                               
							print("No es posible jugar ahi"+'\n'+"Por favor intente una nueva jugada")                     
							continue
						else:
							pygame.draw.circle(pantalla, BLANCO, (ColumnaCirculo[JugadaColumnaJugador], FilaCirculo[Fila]), 25, 0)
							Matrix[Fila][JugadaColumnaJugador]=1
							pygame.display.flip()
							return Matrix, JugadaPrimeraVez, p, q, Linea, JugadaColumnaJugador          #Se le agrega un Return aqui para cuando el jugador termine
          		                                                                                        #su jugada
		# TURNO DEL COMPUTADOR
		elif turno==2:
			# NIVEL BÁSICO
			if nivel==1:
				JugadaColumnaCPU=random.randint(0,6)        #Como es el nivel basico, se hace un random entre 0 y 6 (las posibles columnas)
				Fila=ValidarJugada(Matrix,JugadaColumnaCPU) #Y llama al proc ValidarJugada a ver si hay casillas vacias en esa col 
				if Fila==-1:
					continue                                #Si Fila es -1 es porque no hay casillas libres, entonces repite el proceso
				else:                                 #Como hay una casilla vacia entonces asigna 2 en la casilla y dibuja el circulo
					time.sleep(0.3)                     #Esperara 0.3 segundos antes de ejecutar la jugada
					pygame.draw.circle(pantalla, AZUL, (ColumnaCirculo[JugadaColumnaCPU], FilaCirculo[Fila]), 25, 0)
					Matrix[Fila][JugadaColumnaCPU]=2
					break
			# NIVEL MEDIO
			elif nivel==2:
				time.sleep(0.3)                       #Esperara 0.3 segundos antes de ejecutar la jugada
				if JugadaPrimeraVez==True:            #Si es la primera jugada de la partida, juega una casilla random
					while JugadaPrimeraVez==True:
						if Matrix[p][q]==0:  
							Matrix[p][q]=2
							pygame.draw.circle(pantalla, AZUL, (ColumnaCirculo[q], FilaCirculo[p]), 25, 0)
							JugadaPrimeraVez=False
						elif Matrix[p][q]!=0:
							q=random.randint(0,6)  
					break                                                            #Se le coloca un break para salir del ciclo inicial
				else:
					Linea=DeterminarLinea(N, M, Matrix, p, q, Linea)
					if Linea==0:                              
						q=q+1
						Matrix[p][q]=2
						pygame.draw.circle(pantalla, AZUL, (ColumnaCirculo[q], FilaCirculo[p]), 25, 0)
					elif Linea==1:
						q=q-1
						Matrix[p][q]=2
						pygame.draw.circle(pantalla, AZUL, (ColumnaCirculo[q], FilaCirculo[p]), 25, 0)
					elif Linea==2:
						p=p-1
						Matrix[p][q]=2
						pygame.draw.circle(pantalla, AZUL, (ColumnaCirculo[q], FilaCirculo[p]), 25, 0)
					elif Linea==3:
						p,q=p-1,q+1
						Matrix[p][q]=2
						pygame.draw.circle(pantalla, AZUL, (ColumnaCirculo[q], FilaCirculo[p]), 25, 0)
					elif Linea==4:
						p,q=p-1,q-1
						Matrix[p][q]=2
						pygame.draw.circle(pantalla, AZUL, (ColumnaCirculo[q], FilaCirculo[p]), 25, 0)
					elif Linea==5:  
						Valida=False
						while Valida==False:
							p,q=random.randint(0,N-1), random.randint(0,M-1)
							Valida=DeterminarJugadaValida(N, M, Matrix, p, q) 
							if Valida==False:
								pass
							elif Valida==True:       
								Matrix[p][q]=2
								pygame.draw.circle(pantalla, AZUL, (ColumnaCirculo[q], FilaCirculo[p]), 25, 0)
				break                                                                  #Se le coloca un break para salir del ciclo inicial

		#Tablero Grafico 
		# Cuadrado exterior
		pygame.draw.line(pantalla, VERDE, (130, 90), (130, 620))
		pygame.draw.line(pantalla, VERDE, (1120, 90), (1120, 620))
		pygame.draw.line(pantalla, VERDE, (130, 90), (1120, 90))
		pygame.draw.line(pantalla, VERDE, (130, 620), (1120, 620))

		# Filas
		pygame.draw.line(pantalla, VERDE, (130, 178), (1120, 178))
		pygame.draw.line(pantalla, VERDE, (130, 266), (1120, 266))
		pygame.draw.line(pantalla, VERDE, (130, 354), (1120, 354))         #Esto es para dibujar el tablero 
		pygame.draw.line(pantalla, VERDE, (130, 442), (1120, 442))
		pygame.draw.line(pantalla, VERDE, (130, 530), (1120, 530))

		# Columnas
		pygame.draw.line(pantalla, VERDE, (272, 90), (272, 620))
		pygame.draw.line(pantalla, VERDE, (414, 90), (414, 620))
		pygame.draw.line(pantalla, VERDE, (556, 90), (556, 620))
		pygame.draw.line(pantalla, VERDE, (698, 90), (698, 620))
		pygame.draw.line(pantalla, VERDE, (840, 90), (840, 620))
		pygame.draw.line(pantalla, VERDE, (982, 90), (982, 620))

		pygame.display.flip()
	return Matrix, JugadaPrimeraVez, p, q, Linea, JugadaColumnaJugador


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
		SigueFila=DeterminarJugadaValida (N, M, Matrix, p, q+1)
	elif Linea==1:
		SigueFila=DeterminarJugadaValida (N, M, Matrix, p, q-1) 
	elif Linea==2:
		SigueFila=DeterminarJugadaValida (N, M, Matrix, p-1, q)       #Aqui verifica si puede seguir jugando en la Linea en que esta, si no 
	elif Linea==3:                                                    #SigueFila=False y se le determina una nueva Fila
		SigueFila=DeterminarJugadaValida (N, M, Matrix, p-1, q+1)
	elif Linea==4:
		SigueFila=DeterminarJugadaValida (N, M, Matrix, p-1, q-1)
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
			if i==5:
				Valida=True
			elif i!=5: 
				if Matrix[i+1][j]==1 or Matrix[i+1][j]==2:           #Este proceso es usado unicamente por La computadora en el nivel 2
					Valida= True                                     #Y basica mente revisa si la casilla esta vacia o no, si lo esta luego
				elif Matrix[i+1][j]==0:                              #revisa si tiene una ficha abajo, y si la tiene coloca la ficha ahi
					Valida=False
		elif Matrix[i][j]!=0:
			Valida=False
	elif i<0 or i>N-1 or j<0 or j>M-1:
		Valida=False

	return Valida
 


def ResaltarLinea(a:int, b:int, c:int, d:int, e:int, f:int, g:int, h:int) -> 'void':
	#Precondicion: (%forall i: i={a,b,c,d}: i=1 \/ i=2 )
	#Poscondicion: True

	#Coordenadas de circulos
	ColumnaCirculo=[205,346,486,627,768,909,1050]        #Estas son las coordenadas de los circulos en el tablero
	FilaCirculo=[135,220,310,395,485,575]

	pygame.draw.circle(pantalla, ROJO, (ColumnaCirculo[a], FilaCirculo[b]), 25, 0)
	pygame.draw.circle(pantalla, ROJO, (ColumnaCirculo[c], FilaCirculo[d]), 25, 0)
	pygame.draw.circle(pantalla, ROJO, (ColumnaCirculo[e], FilaCirculo[f]), 25, 0)
	pygame.draw.circle(pantalla, ROJO, (ColumnaCirculo[g], FilaCirculo[h]), 25, 0)

	pygame.display.flip()


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
	elif Ganador==2:
		Ganador2=Ganador2+1

	return Ganador0, Ganador1, Ganador2

def Reanudar (Ganador0:int, Ganador1:int, Ganador2:int) -> int:
	ExisteSave=os.path.isfile('save.txt')                      #Buscamos si existe el archivo 'save.txt', si no existe sale del proceso, si existe se le pregunta si se desea
	if ExisteSave==True:                                       #Seguir jugando la partida anterior
		print("Desea seguir jugando la partida anterior?")
		while True:
			Respuesta=str(input("Si o No?"))
			if Respuesta=="Si":
				Guardado=True
				break
			elif Respuesta=="No":
				Guardado=False
				break
			else:
				print("Solo se puede ingresar Si o No")
				continue
	else:
		Guardado=False
	
	if Guardado==True:
		f=open('save.txt','r')
		Ganador0=int(f.readline().rstrip())                  #Luego si Guardado==True, se carga los scores de la partida pasada
		Ganador1=int(f.readline().rstrip())                  #Y si Guardado==False, no se hace anda y se comienza desde el inicio
		Ganador2=int(f.readline().rstrip())
	else:
		pass
	
	return Ganador0, Ganador1, Ganador2


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                 ALGORITMO PRINCIPAL                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


# VARIABLES Y CONSTANTES

# N: int                           // Constante que representa las filas de la matriz (Para este programa, N sera 6)
# M: int                           // Constante que representa las columnas de la matriz (Para este programa, M sera 7)
# NombreJugador: str               // ENTRADA: guarda el nombre del jugador
# nivel: int                       // ENTRADA: guarda el nivel que desea jugar el usuario
# Tablero:array[0..N)[0..M)of int  // Variable usada para contener la matriz del tablero (posiciones jugadas)
# i: int                           // Variable de la fila en la que juega el usuario (usada para verificar si la jugada es valida)
# turno: int                       // Variable del turno de los jugadores, vale 1 si el turno es del usuario y 2 si es del CPU. 
#                                  // Cambia una vez que pasa por el ciclo (que se obtiene la jugada)
# JugadaPrimeraVez: bool           // Variable usada para ver si el CPU en el nivel medio ya jugo por primera vez
# Linea: int                       // Variable que contiene la Linea que el CPU desea jugar en el nivel medio
# jugada: int                      // Variable que guarda la jugada del jugador y del CPU en el nivel 1
# Ganador: int                     // Variable que contiene el Ganador de la partida (Siempre sera 0 hasta que se decida si se queda asi o cambia a 1 o 2)
# esValida: bool                   // Variable para determinar si la jugada del jugador es valida o no
# siguePartida: bool               // Variable que determina si la partida sigue o ya termino (Cuando se le pregunta al usuario si desea seguir jugando y dice que si, vale True)
# jugarOtra: bool                  // Variable para determinar si se desea jugar otra partida o no
# p: int                           // Variable que contendra la ultima fila jugada por el CPU en el nivel medio
# q: int                           // Variable que contendra la ultima columna jugada por el CPU en el nivel medio
# Ganador0:int                     // Contador de veces que ha quedado en empate la partida
# Ganador1:int                     // Contador de veces que ha ganado el Jugador
# Ganador2:int                     // Contador de veces que ha ganado el computador
# PrimeraPartida: bool             // Esta variable verifica si es la primera partida que se juega entre el computador y el jugador


# INICIALIZACION DE VARIABLES
N=6
M=7
JugadaColumnaJugador=0
Ganador=0
esValida=True
jugarOtra, PrimeraPartida=True,True
Ganador0, Ganador1, Ganador2=0,0,0

#-------------------------
# INTERFAZ GRAFICA        
#-------------------------

# CONSTANTES
# Pantalla
ALTO = 720       # alto de la ventana
ANCHO = 1280     # ancho de la ventana
FPS = 30         # frames per second
# Colores 
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

# Inicializar la pantalla del juego
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'                  # Centrar la ventana a la hora de abrirse
pantalla = pygame.display.set_mode((ANCHO, ALTO))       # Configurando la pantalla
pygame.display.set_caption("Juego Equipo 4")            # Coloca titulo a nuestra pantalla
reloj = pygame.time.Clock() 



Ganador0,Ganador1,Ganador2=Reanudar(Ganador0, Ganador1, Ganador2)
# CICLO PRINCIPAL DEL PROGRAMA:
while jugarOtra==True:
	Ganador, nombreJugador, nivel, Tablero, Linea, q, p, JugadaPrimeraVez, turno = InicializarPartida(pantalla, PrimeraPartida, Ganador, N, M) 
	siguePartida=True
	while siguePartida==True:                                                                                                                                                                     
		Tablero, JugadaPrimeraVez, p, q, Linea, JugadaColumnaJugador = ObtenerJugada(JugadaColumnaJugador, nivel, turno, nombreJugador, N, M, Tablero, JugadaPrimeraVez, Linea, p, q, Ganador0, Ganador1, Ganador2)   
		Ganador = DeterminarGanador(N,M,turno,Tablero, Ganador)  
		siguePartida = DeterminarPartidaTerminada(N, M, Ganador, Tablero, siguePartida)                  
		turno = CambiarTurno(turno)    

	DesplegarGanador(nombreJugador, Ganador) 
	Ganador0, Ganador1, Ganador2 = ContarGanadorPartida(Ganador, Ganador0, Ganador1, Ganador2)
	PrimeraPartida, jugarOtra = otraPartida(Ganador0,Ganador1,Ganador2)  

DesplegarResultadoFinal(Ganador0, Ganador1, Ganador2) 
pygame.quit()
