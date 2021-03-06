# Juego4enLineaEquipo04.py
#
# Descripción: Este es el algoritmo que sigue el juego  Cuatro en linea, que consiste en una matriz 6x7 y dos "fichas" (para 2 jugadores) 
#              que tendran el valor 1 y 2 cuando ocupen una posicion en la Matriz, el objetivo del juego es completar una linea de 4 fichas 
#              de forma vertical, horizontal o Diagonal.
#
# Autores: Pietro Iaia
#          Antonella Requena
#
# Última fecha de modificación: 06/04/2018


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
    cota=N-i
    #Invariante y cota
    #assert((any((Matrix[l][k]==turno and Matrix[l+1][k]==turno and Matrix[l+2][k]==turno and Matrix[l+3][k]==turno for k in range(j+1) for l in range(i+1)))==(Ganador==turno)) and 0<=i<N-3 and 0<=j<M)
    assert(cota>=0)
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
        #Invariante y cota
        #assert((any((Matrix[l][k]==turno and Matrix[l+1][k]==turno and Matrix[l+2][k]==turno and Matrix[l+3][k]==turno for k in range(j+1) for l in range(i+1)))==(Ganador==turno)) and 0<=i<N-3 and 0<=j<M)
        assert(cota>=N-i)
        cota=N-i
        assert(cota>=0)
 
    # LINEA HORIZONTAL
    j=0
    cota=M-j
    #Invariante y cota
    #assert((any((Matrix[l][k]==turno and Matrix[l][k+1]==turno and Matrix[l][k+2]==turno and Matrix[l][k+3]==turno for k in range(j+1) for l in range(i+1)))==(Ganador==turno)) and 0<=i<N and 0<=j<M-3)
    assert(cota>=0)
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
        #Invariante y cota
        #assert((any((Matrix[l][k]==turno and Matrix[l][k+1]==turno and Matrix[l][k+2]==turno and Matrix[l][k+3]==turno for k in range(j+1) for l in range(i+1)))==(Ganador==turno)) and 0<=i<N and 0<=j<M-3)
        assert(cota>=M-j)
        cota=M-j
        assert(cota>=0)

    # LINEA DIAGONAL DERECHA
    i=0
    cota=3-i
    #Invariante y cota
    #assert((any((Matrix[l][k]==turno and Matrix[l+1][k+1]==turno and Matrix[l+2][k+2]==turno and Matrix[l+3][k+3]==turno for k in range(j+1) for l in range(i+1)))==(Ganador==turno)) and 0<=i<3 and 0<=j<4)
    assert(cota>=0)
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
        #Invariante y cota
        #assert((any((Matrix[l][k]==turno and Matrix[l+1][k+1]==turno and Matrix[l+2][k+2]==turno and Matrix[l+3][k+3]==turno for k in range(j+1) for l in range(i+1)))==(Ganador==turno)) and 0<=i<3 and 0<=j<4)
        assert(cota>=3-i)
        cota=3-i
        assert(cota>=0)
    
    # LINEA DIAGONAL IZQUIERDA
    i=0
    cota=3-i
    #Invariante y cota
    #assert((any((Matrix[l][k]==turno and Matrix[l+1][k-1]==turno and Matrix[l+2][k-2]==turno and Matrix[l+3][k-3]==turno for k in range(j+1) for l in range(i+1)))==(Ganador==turno)) and 0<=i<3 and 0<j<6)
    assert(cota>=0)
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
        #Invariante y cota
        #assert((any((Matrix[l][k]==turno and Matrix[l+1][k-1]==turno and Matrix[l+2][k-2]==turno and Matrix[l+3][k-3]==turno for k in range(j+1) for l in range(i+1)))==(Ganador==turno)) and 0<=i<3 and 0<j<6)
        assert(cota>=3-i)
        cota=3-i
        assert(cota>=0)

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
    #Precondicion
    assert(any((Matrix[i][j]!=0 for i in range(N)) for j in range(M)))

    print("¿Desea guardar su partida? [y/n]")
    while True:
        Respuesta=str(input("y o n "+'\n'))
        try:
            assert(Respuesta=='y' or Respuesta=='n')
            break
        except:
            print("Solo se puede ingresar 'y' si quiere o 'n' sino")  #Si se escribe algo mas que 'y' o 'n' informa que solo puede escoger entre esos dos
    if Respuesta=="y":
        siguePartida=1
        GuardarArchivo(Matrix,Ganador0,Ganador1,Ganador2,siguePartida)
        pygame.quit()
        sys.exit()  
    elif Respuesta=="n":
        pygame.quit()                              #Se cierra el juego y no se guarda nada si se selecciona 'n'
        sys.exit()
    #Postcondicion
    assert(True)

# PROCEDIMIENTO PARA GUARDAR LA PARTIDA
def GuardarArchivo(Matrix:[int],Ganador0:int,Ganador1:int,Ganador2:int,siguePartida:int) -> 'void':
    #Descripcion: Recibe el estado del tablero y los contadores por ganador (0 es empatadas, 1 es usuario y 2 es computador)
    #recibe un bool para saber si escribe el estado del tablero o no. Si la partida finalizo, no se guarda el tablero.
    #Precondicion:
    assert(any((Matrix[i][j]!=0 for i in range(N)) for j in range(M)))

    with open('save.txt','w') as file:
        file.write("Empatadas: "+str(Ganador0)+'\n')
        file.write("Usuario: "+str(Ganador1)+'\n')                #Se abre el 'save.txt' y se escribe los resultados totales en cada fila
        file.write("Computador: "+str(Ganador2)+'\n')
        file.write("Partida: "+str(siguePartida)+'\n')
        if siguePartida:
            for row in Matrix:
                file.write(" ".join(list(map(str, row)))+'\n')
    #Postcondicion
    assert(True)
                                                                  


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
def otraPartida(Ganador0:int,Ganador1:int,Ganador2:int,Matrix:[int]) -> (bool,bool):
    #Descripcion: Las variables de entrada son los contadores de cada ganador por partida, se reciben
    #             para poder ser almacenados en el archivo. Retorna 2 booleanos que dicen si es la primera
    #             partida y si el usuario quiere seguir jugando otra partida

    #Precondicion:
    assert(any((Matrix[i][j]!=0 for i in range(N)) for j in range(M)))  

    PrimeraPartida=False                               #Se le asigna PrimeraPartida=False ya que termino la primera partida entre el jugador y
    print("La partida ha finalizado")                  #la Computadora
    print("¿Desea jugar otra partida?") 

    while True:
        y=str(input("Si o No?"+'\n'))
        y=y.lower() 
        if y=="si":
            jugarOtra=True                              #Si se escoge Si, empieza el ciclo denuevo, si se escoge que No se le pedira si desea
            break                                       #Guardar la partida
        elif y=="no": 
            print("¿Desea Guardar su partida?")
            while True:
                Respuesta=str(input("Si o No?"+'\n'))
                Respuesta=Respuesta.lower()
                if Respuesta=="si":
                    siguePartida=0
                    GuardarArchivo(Matrix,Ganador0,Ganador1,Ganador2,siguePartida)         
                    break   
                elif Respuesta=="no":                     
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
    assert((jugarOtra==True and y=="si") or (jugarOtra==False and y=="no"))

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

# PROCEDIMIENTO PARA DIBUJAR EL TABLERO
def DibujarTablero():
    #Descripcion: Este procedimiento implementa las funcionalidades de pygame para dibujar el tablero
#Precondicion: No hay

    # Cuadrado exterior
    pygame.draw.line(pantalla, VERDE, (130, 90), (130, 620))    #dibuja las lineas con sus respectivas coordenadas
    pygame.draw.line(pantalla, VERDE, (1120, 90), (1120, 620))
    pygame.draw.line(pantalla, VERDE, (130, 90), (1120, 90))
    pygame.draw.line(pantalla, VERDE, (130, 620), (1120, 620))

    # Filas
    pygame.draw.line(pantalla, VERDE, (130, 178), (1120, 178))
    pygame.draw.line(pantalla, VERDE, (130, 266), (1120, 266))
    pygame.draw.line(pantalla, VERDE, (130, 354), (1120, 354))        
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
#Postcondicion: No hay

# PROCEDIMIENTO PARA INICIALIZAR LA PARTIDA
def InicializarPartida(pantalla:int,PrimeraPartida:bool, Ganador:int, N:int, M:int) -> (str,int,bool):
    """ Descripcion: Este procedimiento inicializa el tablero, recibe como parametros la variable pantalla, utilizada para
        la funcion de fill de pygame para poner la pantalla de un color. Recibe el bool de primera partida ya que si es 
        la primera partida, sino, recibe el parametro ganador dependiendo de su valor (1 o 2) le asignara el turno al ganador 
        correspondiente. Si es 0 empezara el computador. N y M son los tamaños de la matriz. En este subprograma se 
        le pide al usuario su nombre y el nivel que desea jugar. Retorna el tablero (matriz) con todas las casillas en 0, 
        el nombre del jugador, el nivel que desea jugar, las variables de la primera casilla a jugar del computador y un 
        booleano que indica que ya se hizo la primera jugada
    """
    #Precondicion
    assert(N>0 and M>0 and 0<=Ganador<=2)

    #ENTRADA DE DATOS
    while True:
        nombreJugador=str(input("Ingrese su nombre: "))
        try:
            assert(len(nombreJugador)>=3)             #Programa robusto
            break
        except:
            print("Por favor, introduzca su nombre")

    print("Indique  el nivel que desea jugar")
    print("Nivel Básico: Tipee 1.")                                 #Aqui se le pide al usuario ingresar su nombre y un nivel
    print("Nivel Medio: Tipee 2. ")                                  #Si tipea algo mas que 1 o 2 en nivel, se le avisara que solo
    while True:                                                     #puede tipear Nivel 1 o Nivel 2
        nivel=int(input("Nivel: "))
        try:
            assert(1<=nivel<=2)
            break
        except:
            print("Solo puede ingresar Nivel 1 o Nivel 2")

    #INICIALIZACION DEL TABLERO
    pantalla.fill(NEGRO)
    pygame.display.flip()
    DibujarTablero()
    Matrix=[[0 for x in range(M)] for x in range(N)]             #Pone todas las casillas en 0 para iniciar la partida


    
    #Variables para el nivel medio del CPU
    Linea=5                                            #Linea=5 ya que se necesitara mas adelante en el codigo que sea asi
    q,p= random.randint(0,6),5                         #p y q son las jugadas de la computadora en el nivel medio. Estas variables son para guardar su ultima jugada.
    JugadaPrimeraVez=True                              #JugadaPrimeraVez=True ya que seria la primera vez que juega la computadora en esta partida

    #Turnos
    if PrimeraPartida==True:
        turno=2
    else:                                              #Si es la Primera Partida de la sesion, se le asigna el turno a la computadora
        if Ganador==1:                                 #Si no, se verifica quien es el ganador de la partida pasada y empezaria el
            turno=1                                    #Y si quedo empatado, empieza la computadora
            Ganador=0                                  
        elif Ganador==2 or Ganador==0:                 #Se le pone Ganador=0 ya que al iniciar la partida otra vez, se debe reiniciar esa variable
            turno=2
            Ganador=0
    #Postcondicion: 
    assert(all((Matrix[i][j]==0 for i in range(N)) for j in range(M)))
    
    return Ganador, nombreJugador, nivel, Matrix, Linea, q, p, JugadaPrimeraVez, turno

# FUNCION PARA VALIDAR LA JUGADA DEL USUARIO
def ValidarJugada(Matrix:[int], Columna:int) -> bool:
    # Descripcion: Recibe la matriz del tablero y la columna que quiere jugar el usuario
    # chequea si la fila de dicha columna no esta llena

    #Precondicion
    assert(0<=Columna<=6)

    Fila=5
    cota=Fila
    #Invariante y cota
    assert(-1<=Fila<=5)
    assert(cota>=-1)
    while Fila>=0 and Matrix[Fila][Columna]!=0: #Revisa Fila por fila en la columna que jugo el usuario hasta que encuentre una vacia
        Fila=Fila-1                             #Si Fila==-1 es porque recorrio toda la fila (de la posicion 5 a la 0)
        #Invariante y cota en cada iteracion
        assert(-1<=Fila<=5)
        assert(cota>=Fila)
        cota=Fila
        assert(cota>=-1)         
    #Postcondicion
    assert((Fila==-1 and all(Matrix[Fila][Columna]!=0 for Fila in range(N)) ) or (0<=Fila<=5 and any(Matrix[Fila][Columna]==0 for Fila in range(N))))

    # Salida 
    return Fila

# PROCEDIMIENTO PARA PREGUNTAR AL USUARIO SI QUIERE SEGUIR JUGANDO
def seguirJugando(turno:int, primeraJugadaUsuario:bool,Ganador0:int,Ganador1:int,Ganador2:int,Matrix:[int] )-> bool:
    # Descripcion: Este procedimiento recibe el turno que debe ser el del usuario (1), si no es, no hara nada, recibe los 
    # contadores de ganador por partida para luego poder pasarselo al procedimiento QuitGame y recibe la Matriz del tablero
    # para pasarelo a QuitGame tambien. Se le pregunta al usuario por un mensaje en pantalla si quiere seguir jugando, este proc
    # es llamado cada vez que se obtiene jugada, si el usuario responde que no, se llama a QuitGame, si dice que si, se sigue jugando
    # la variable primeraJugadaUsuario es un bool para que este mensaje no aparezca la primera vez que juegue el usuario 
    if turno == 1:
        if not primeraJugadaUsuario:      #Como no es la primera jugada, ya puede preguntar si quiere seguir jugando
            print("¿Desea seguir jugando?")
            while True:
                y=input("si o no? ")
                y=y.lower()
                try:
                    assert(y=="si" or y=="no")
                    break
                except:
                    print("Debe responder si o no")     #Version robusta
                    continue
            if y=="no":
                QuitGame(Ganador0,Ganador1,Ganador2,Matrix) #Se llama a QuitGame

            return False    #retorna false porque ya primeraJugadaUsuario se hizo 
        else:
            return False
    return primeraJugadaUsuario  #como no era el turno del usuario, no se cambia el valor del bool

# PROCEDIMIENTO PARA DIBUJAR CIRCULOS
def DibujarCirculo(Columna:int,Fila:int,turno:int)->'void':
    #Descripcion: Implementacion de las funcionalidades de pygame (draw.circle dibuja un circulo) para 
    # dibujar los circulos que representan las fichas. Recibe la columna, la fila donde dibujara el circulo
    # y el turno para asignar el color respectivo, si turno es 1 el circulo es blanco y si turno es 2 es azul

    #Precondicion
    assert(1<=turno<=2 and 0<=Columna<=6 and 0<=Fila<=5)

    #Coordenadas de circulos
    ColumnaCirculo=[205,346,486,627,768,909,1050]        #Estas son las coordenadas de los circulos en el tablero
    FilaCirculo=[135,220,310,395,485,575]

    color = AZUL if turno == 2 else BLANCO      #Asigna el color al circulo dependiendo del turno

    pygame.draw.circle(pantalla, color, (ColumnaCirculo[Columna], FilaCirculo[Fila]), 25, 0) #Dibuja el circulo 
    pygame.display.flip()

    #Postcondicion: No hay

# PROCEDIMIENTO PARA DIBUJAR LINEAS DE SELECCION
def DibujarLinea(L:int)->'void':
    #Descripcion: Recibe como parametro L que es la linea (o columna) donde se para el usuario, esto es para dibujar
    # las lineas de seleccion
    #Precondicion
    assert(0<=L<=6)

    ini = [(i, 50) for i in range(130, 977, 141)] 
    fin = [(i, 50) for i in range(271, 1118, 141)]

    pygame.draw.line(pantalla, NEGRO, ini[(L+6)%7], fin[(L+6)%7], 7)
    pygame.draw.line(pantalla, BLANCO, ini[L], fin[L], 7)

    pygame.display.flip()

    #Postcondicion: No hay


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

    # Hacer que el juego corrar a una velocidad que deseemos
    reloj.tick(FPS)

    # TURNO DEL USUARIO
    if turno==1:
        print("Su turno, " + nombreJugador)
        jugada = False
        while not jugada:
            for evento in pygame.event.get():
                # Si el evento que esta ocurriendo es que se acabo el juego, entonces cerrarlo
                if evento.type == pygame.QUIT:
                    QuitGame(Ganador0, Ganador1, Ganador2,Matrix)
                # SI EL EVENTO ES MOVERSE ENTRE COLUMNAS
                elif evento.type == pygame.MOUSEBUTTONDOWN:          #Dibujar una Linea cuando se presiona el mouse, y borra la anterior dibujada
                    if JugadaColumnaJugador==6:
                        JugadaColumnaJugador=0
                    else:                                                 #Cada vez que se oprima el mouse, cambia de Columna, cuando llegue a la 6, se devuelve
                        JugadaColumnaJugador=JugadaColumnaJugador+1       #a la 0

                    DibujarLinea(JugadaColumnaJugador)


                #Dibuja un circulo dependiendo de donde este la posicion de la Linea

                # SI EL EVENTO ES SELECCIONAR LA COLUMNA (HACER JUGADA)
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:                                     #ADVERTENCIA: No oprimir el espacio una vez terminada una partida ya que
                        Fila=ValidarJugada(Matrix,JugadaColumnaJugador)                  #el programa lo tomara en cuenta y jugara por usted si selecciona
                        if Fila==-1:                                                     #volver a jugar
                            print("No es posible jugar ahi"+'\n'+"Por favor intente una nueva jugada")                     
                            continue
                        else:
                            DibujarCirculo(JugadaColumnaJugador, Fila, turno)
                            Matrix[Fila][JugadaColumnaJugador] = 1
                            return Matrix, JugadaPrimeraVez, p, q, Linea, JugadaColumnaJugador      #Se le agrega un Return aqui para cuando el jugador termine su jugada
            pygame.display.flip()
                                                                                                                    
    # TURNO DEL COMPUTADOR
    elif turno==2:
        print("Juega la pc")
        # NIVEL BÁSICO
        if nivel==1:
            while True:
                JugadaColumnaCPU=random.randint(0,6)        #Como es el nivel basico, se hace un random entre 0 y 6 (las posibles columnas)
                Fila=ValidarJugada(Matrix,JugadaColumnaCPU) #Y llama al proc ValidarJugada a ver si hay casillas vacias en esa col 
                                                      #Si Fila es -1 es porque no hay casillas libres, entonces repite el proceso
                if Fila != -1:                                   #Como hay una casilla vacia entonces asigna 2 en la casilla y dibuja el circulo
                    time.sleep(0.3)                     #Esperara 0.3 segundos antes de ejecutar la jugada
                    DibujarCirculo(JugadaColumnaCPU,Fila,turno)
                    Matrix[Fila][JugadaColumnaCPU]=2
                    break
        # NIVEL MEDIO
        elif nivel==2:
            time.sleep(0.3)                      #Esperara 0.3 segundos antes de ejecutar la jugada
            if JugadaPrimeraVez==True:            #Si es la primera jugada de la partida, juega una casilla random
                while JugadaPrimeraVez==True:
                    if Matrix[p][q]==0:  
                        Matrix[p][q]=2
                        DibujarCirculo(q,p,turno)
                        JugadaPrimeraVez=False   #Ya jugo la primera vez, le asigna False a este booleano
                    else:
                        q=random.randint(0,6)     #Como no hay una casilla vacia donde quiso jugar, hace un random de otra fila
            else:                                     #Como ya no es la primera jugada, entonces procede a la estrategia
                Linea=DeterminarLinea(N, M, Matrix, p, q, Linea)
                if Linea==0:                          #En estas guardias ya escogio la linea que intentara construir                           
                    q=q+1                             #Linea 0 es linea horizontal hacia la derecha
                    Matrix[p][q]=2                    #Se aumenta q porque esta barriendo las columnas hacia adelante
                elif Linea==1:                        #Linea 1 es linea horizontal hacia la izquierda
                    q=q-1                             #Se disminuye q porque esta barriendo las columnas hacia atras
                    Matrix[p][q]=2
                elif Linea==2:                        #Linea 2 es linea vertical
                    p=p-1                             #Se disminuye p porque esta barriendo las filas hacia arriba (va de 5 a 0)
                    Matrix[p][q]=2
                elif Linea==3:                        #Linea 3 es linea diagonal derecha
                    p,q=p-1,q+1                       #p decrece porque se barren las filas hacia arriba y q crece porque
                    Matrix[p][q]=2                    #se desplaza hacia la derecha
                elif Linea==4:                        #Linea 4 es linea diagonal izquierda
                    p,q=p-1,q-1                       #ambos decrecen porque se barren las filas hacia arriba y las
                    Matrix[p][q]=2                    #columnas hacia atras
                elif Linea==5:                        #Linea auxiliar que indica que no puede construir ninguna linea
                    Valida=False                      #a partir de la casilla donde esta
                    while not Valida:
                        p,q=random.randint(0,N-1), random.randint(0,M-1)    #Como no puede seguir jugando alli, busca de manera
                        Valida=DeterminarJugadaValida(N, M, Matrix, p, q)   #aleatoria otra casilla donde pueda construir una linea       
                Matrix[p][q]=2                                          #sale del ciclo porque Valida es True y ya puede ocupar la casilla
                DibujarCirculo(q,p,turno)

    #Postcondicion
    assert((turno==1 and Matrix[Fila][JugadaColumnaJugador]==1) or (turno==2 and nivel==2 and Matrix[p][q]==2) 
    or (turno==2 and nivel==1 and Matrix[Fila][JugadaColumnaCPU]==2))
    return Matrix, JugadaPrimeraVez, p, q, Linea, JugadaColumnaJugador

# FUNCION PARA DETERMINAR LA LINEA QUE INTENTARA CONSTRUIR EL COMPUTADOR (NIVEL MEDIO)
def DeterminarLinea(N:int, M:int, Matrix:int, p:int, q:int, Linea:int) -> int:
    """ Descripcion: Esta funcion es la que desarrolla la estrategia a seguir por el computador en el nivel medio
        recibe como parametros N y M que son el tama;o del arreglo, Matrix que es la matriz del tablero, p y q que representan
        la fila y la columna de la casilla de la ultima jugada del computador, y linea es la linea que intenta construir el computador.
        Esto retorna un entero entre 0 y 5 que representara la linea que intentara construir el computador. 
        Tiene 5 variables booleanas enumeradas del 0 al 4 que corresponden a las lineas que puede intentar construir el computador
        Para saber si es valida dicha linea, llama a la funcion DeterminarJugadaValida que fue creada para este nivel, lo que hace
        es chequear si es valido jugar en las casillas adyacentes, es decir, la de su derecha (0) , izquierda (1), arriba (2), 
        diagonal derecha (3) y diagonal izquierda (4). Al recibir linea, chequea si puede seguir construyendo dicha linea, esto
        lo verifica con la variable local SigueFila, al llamar al procedimiento que chequea si es valido seguir jugando en las casillas
        adyacentes. Finalmente, si sigueFila es True es porque puede continuar intentando construir dicha linea, si es false, 
        buscara cual de las variables Valida es true para luego asignarle su respectivo indice a linea. Si no puede hacer esto porque 
        no hay ninguna casilla vacia adyacente, entonces se le asigna a linea el valor 5 que lo que hara en otro procedimiento es buscar una
        casilla aleatoria donde poder intentar construir una linea nuevamente.   
    """
    #Precondicion:
    assert(0<=Linea<=5 and N>0 and M>0) 

    #VARIABLES
    # Valida0, Valida1, Valida2, Valida3, Valida4, SigueFila :bool  #Estas variables son para verificar que linea es valida construir

    Valida0=DeterminarJugadaValida(N, M, Matrix, p, q+1)  
    Valida1=DeterminarJugadaValida(N, M, Matrix, p, q-1)  
    Valida2=DeterminarJugadaValida(N, M, Matrix, p-1, q)           #En estos procesos se verfica si cada posible fila tiene ficha abajo.
    Valida3=DeterminarJugadaValida(N, M, Matrix, p-1, q+1) 
    Valida4=DeterminarJugadaValida(N, M, Matrix, p-1, q-1) 
    SigueFila=False                                                #Se le asigna SigueFila=False para inicializarla, puede que su valor cambie en el if de abajo

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


    if SigueFila:
        pass
    elif not SigueFila:                               #Si al determinar que puede seguir en la misma fila SigueFila==True, entonces
        if Valida0:                                #No hay necesidad de cambiarle la Linea y hacemos pass
            Linea=0                                      #Pero si SigueFila==False es porque no puede seguir en esa Linea y se verifica en cual direccion
        elif Valida1:                              #desea empezar a construir y al encontrar una se le asigna la Linea correspondiente
            Linea=1                                      #Si no puede construir para ninguna direccion desde donde esta, se le asigna Linea=5
        elif Valida2:
            Linea=2
        elif Valida3:
            Linea=3
        elif Valida4:
            Linea=4
        else:                               
            Linea=5
    #Postcondicion
    assert((Valida0 and Linea==0) or (Valida1 and Linea==1) or (Valida2 and Linea==2) or (Valida3 and Linea==3) or (Valida4 and Linea==4) 
        or (not Valida0 and not Valida1 and not Valida2 and not Valida3 and not Valida4 and Linea==5) )
    return Linea

# PROCEDIMIENTO PARA DETERMINAR JUGADA VALIDA DEL COMPUTADOR
def DeterminarJugadaValida (N:int, M:int, Matrix:int, i:int, j:int) -> bool:
    #Descripcion: Este procedimiento recibe la matriz del tablero y los indices que corresponden a la fila y columna en donde 
    #quiere jugar el computador y con un if primero chequea si i y j no se salen del rango, luego, si la casilla en esa posicion
    #donde quiere jugar esta vacia, luego chequea, si esta en la fila 5, dice que es Valida jugar alli, si no, verifica si tiene alguna
    #casilla ocupada debajo, y de ser asi, entonces retorna Valida true. Si se sale del rango de la matriz, valida es false

    #Precondicion:
    assert(any((Matrix[i][j]!=0 for i in range(N)) for j in range(M)))

    if i>=0 and i<=N-1 and j>=0 and j<=M-1:
        if Matrix[i][j]==0:
            if i==5:
                Valida=True
            elif i!=5: 
                if Matrix[i+1][j]!=0:                                #Este proceso es usado unicamente por La computadora en el nivel 2
                    Valida= True                                     #Y basica mente revisa si la casilla esta vacia o no, si lo esta luego
                else:                                                #revisa si tiene una ficha abajo, y si la tiene coloca la ficha ahi
                    Valida=False
        elif Matrix[i][j]!=0:
            Valida=False
    else:
        Valida=False
    
    #Postcondicion
    #assert((Matrix[i][j]==0 and Valida==True and i==5) or (Matrix[i][j]==0 and Valida==True and Matrix[i+1][j]!=0) or (Matrix[i][j]==0 and Valida==False and Matrix[i+1][j]==0) or (Matrix[i][j]!=0 and Valida==False))
    return Valida

# PROCEDIMIENTO PARA RESALTAR LA LINEA GANADORA 
def ResaltarLinea(a:int, b:int, c:int, d:int, e:int, f:int, g:int, h:int) -> 'void':
    #Descripcion: Este procedimiento resalta la linea ganadora coloreando los circulos de rojo
    #Los parametros que recibe corresponden a las casillas de la fila en que esta cada circulo (a,c,e y g)
    # y las casillas de la columna (b,d,f,h)

    #Precondicion: 
    assert(True)

    #Coordenadas de circulos
    ColumnaCirculo=[205,346,486,627,768,909,1050]        #Estas son las coordenadas de los circulos en el tablero
    FilaCirculo=[135,220,310,395,485,575]

    pygame.draw.circle(pantalla, ROJO, (ColumnaCirculo[a], FilaCirculo[b]), 25, 0)
    pygame.draw.circle(pantalla, ROJO, (ColumnaCirculo[c], FilaCirculo[d]), 25, 0)
    pygame.draw.circle(pantalla, ROJO, (ColumnaCirculo[e], FilaCirculo[f]), 25, 0)
    pygame.draw.circle(pantalla, ROJO, (ColumnaCirculo[g], FilaCirculo[h]), 25, 0)

    pygame.display.flip()

    #Postcondicion
    assert(True)

# PROCEDIMIENTO PARA DESPLEGAR EL RESULTADO FINAL
def DesplegarResultadoFinal(Ganador0:int, Ganador1:int, Ganador2:int) -> 'Void':
    #Descripcion: Este procedimiento imprime en pantalla el resultado final 
    #tras haber jugado las partidas, los parametros que recibe son los contadores de
    #las partidas ganadas por cada jugador, y simplemente los imprime con un mensaje
    #en pantalla

    #Precondicion: 
    assert(Ganador1>=0 and Ganador2>=0 and Ganador0>=0)

    print("El resultado final es:")
    print("Total partidas ganadas por "+str(nombreJugador))
    print(Ganador1)
    print("Total partidas ganadas por la computadora ")
    print(Ganador2)
    print("Total partidas empatadas")
    print(Ganador0)

    #Postcondicion
    assert(True)

# PROCEDIMIENTO PARA CONTAR EL GANADOR POR PARTIDA
def ContarGanadorPartida(Ganador:int,Ganador0:int,Ganador1:int,Ganador2:int) -> int:
    #Este procedimiento es un contador que recibe al ganador de la partida actual
    #y si es 0, a ganador0 (empate) le suma 1 y asi sucesivamente con cada ganador.
    #retorna estos contadores

    #Precondicion: 
    assert(0<=Ganador<=2)
    if Ganador==0:
        Ganador0=Ganador0+1
    elif Ganador==1:
        Ganador1=Ganador1+1
    elif Ganador==2:
        Ganador2=Ganador2+1
    #Postcondicion: 
    assert(Ganador0>=0 and Ganador1>=0 and Ganador2>=0)

    return Ganador0, Ganador1, Ganador2

# PROCEDIMIENTO PARA REANUDAR LA PARTIDA
def Reanudar() -> (int, int,int,[[int]],bool):
    #Descripcion: Este procedimiento busca si existe un archivo save.txt, de ser
    #asi, le pregunta al jugador si desea seguir jugando la partida anterior, porque
    #esto indica que hay una partida guardada
    #Si el usuario quiere jugar con ese registro, se le asigna a un bool true para luego leer el archivo
    #Si dice que no, no se lee el archivo
    ExisteSave=os.path.isfile('save.txt')                          #Buscamos si existe el archivo 'save.txt', si no existe sale del proceso, si existe se le pregunta si se desea
    if ExisteSave:    
        print("Se ha detectado una partida guardada")              #Seguir jugando la partida anterior
        print("¿Desea cargar la partida?")
        while True:
            Respuesta=str(input("Si o No?"))
            Respuesta=Respuesta.lower()
            if Respuesta=="si":
                Guardado=True
                break
            elif Respuesta=="no":
                Guardado=False
                break
            else:
                print("Solo se puede ingresar Si o No")
                continue
    else:
        Guardado=False

    Matrix = []                          #Se inicializa la matriz que se va a leer
    Ganador0,Ganador1,Ganador2 = 0,0,0
    if Guardado:
        with open('save.txt','r') as file: 
            Ganador0=int(file.readline().split(" ")[1].rstrip())                  #Luego si Guardado==True, se carga los scores de la partida pasada
            Ganador1=int(file.readline().split(" ")[1].rstrip())                  #Y si Guardado==False, no se hace anda y se comienza desde el inicio
            Ganador2=int(file.readline().split(" ")[1].rstrip())
            statusPartida=int(file.readline().split(" ")[1].rstrip())             #Esta variable es para chequear si la partida que se guardo
            if statusPartida == 1:                                                #se guardo con tablero, de ser asi, se lee la matriz
                for i in range(6):
                    Matrix.append(list(map(int,file.readline().rstrip().split(" "))))  #se recorre la matriz y se le asigna los valores que tiene la lista
                                                                                       #del archivo, map lo que hace es convertir los strings del archivo en enteros
    return Ganador0, Ganador1, Ganador2,Matrix,Guardado                                #para poder asignarselos a la matriz


def Bienvenida() -> 'void':
    print('\n'+"******************************************************************************************")
    print("*                                       BIENVENIDO                                       *")
    print("*                                      FOUR IN LINE                                      *")
    print("*                                        Equipo 04                                       *")
    print("******************************************************************************************")
    print("CONTROLES: " +'\n'+ "Mouse: seleccionas la columna deseada haciendo click del mouse hasta la posicion que desees")
    print("Barra Espaciadora: Al presionarla, se coloca la ficha"+'\n '+ "(ADVERTENCIA: No presionar luego de terminada la partida o jugara por usted si desea volver a jugar)")
    print('\n'+"Ficha azul: Ficha del computador")
    print('\n'+"Ficha blanca: Ficha del Jugador"+'\n')


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                 ALGORITMO PRINCIPAL                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

#-------------------------#
# INTERFAZ GRAFICA        #
#-------------------------#

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


# VARIABLES Y CONSTANTES

# N: int                           // Constante que representa las filas de la matriz (Para este programa, N sera 6)
# M: int                           // Constante que representa las columnas de la matriz (Para este programa, M sera 7)
# NombreJugador: str               // ENTRADA: guarda el nombre del jugador
# nivel: int                       // ENTRADA: guarda el nivel que desea jugar el usuario
# Tablero:array[0..N)[0..M)of int  // Variable usada para contener la matriz del tablero (posiciones jugadas)
# TableroG:array[0..N)[0..M)of int // Variable usada para contener llenar la matriz del tablero que quedo de la partida anterior
# turno: int                       // Variable del turno de los jugadores, vale 1 si el turno es del usuario y 2 si es del CPU. 
#                                  // Cambia una vez que pasa por el ciclo (que se obtiene la jugada)
# JugadaPrimeraVez: bool           // Variable usada para ver si el CPU en el nivel medio ya jugo por primera vez
# primeraJugadaUsuario: bool       // Variable usada para ver si el usuario ya jugo por primera vez
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
Tablero=[]

Bienvenida()
Ganador0,Ganador1,Ganador2,TableroG,Guardado = Reanudar()

# CICLO PRINCIPAL DEL PROGRAMA:
while jugarOtra:
    Ganador, nombreJugador, nivel, Tablero, Linea, q, p, JugadaPrimeraVez, turno = InicializarPartida(pantalla, PrimeraPartida, Ganador, N, M) 
    if TableroG:
        Tablero = TableroG
        for i in range(N):
            for j in range(M):
                if Tablero[i][j]!=0:
                    DibujarCirculo(j,i,Tablero[i][j])
        turno = 1
        JugadaPrimeraVez = False 
    siguePartida=True
    primeraJugadaUsuario = True
    while siguePartida:
        primeraJugadaUsuario = seguirJugando(turno, primeraJugadaUsuario,Ganador0,Ganador1,Ganador2,Tablero)                                                                                                                                                                  
        Tablero, JugadaPrimeraVez, p, q, Linea, JugadaColumnaJugador = ObtenerJugada(JugadaColumnaJugador, nivel, turno, nombreJugador, N, M, Tablero, JugadaPrimeraVez, Linea, p, q, Ganador0, Ganador1, Ganador2)   
        Ganador = DeterminarGanador(N,M,turno,Tablero, Ganador)  
        siguePartida = DeterminarPartidaTerminada(N, M, Ganador, Tablero, siguePartida)                  
        turno = CambiarTurno(turno)    

    DesplegarGanador(nombreJugador, Ganador) 
    Ganador0, Ganador1, Ganador2 = ContarGanadorPartida(Ganador,Ganador0,Ganador1,Ganador2)
    PrimeraPartida, jugarOtra = otraPartida(Ganador0,Ganador1,Ganador2,Tablero)
    TableroG = []
DesplegarResultadoFinal(Ganador0, Ganador1, Ganador2) 
pygame.quit()