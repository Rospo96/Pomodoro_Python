# FUNCIONES IMPORTADAS
import time

import funcion_descanso_5_min
"""
Vamor a crear la aplicación Pomodoro en Python.

El metodo Pomodoro consiste en un contador que dura 25 minutos exactos. Y otro contador que dura 5 minutos

Tenemos que tener un activador el cual nos preguntará si queremos iniciar el Pomodoro de 25 minutos
Una vez iniciado el mismo va a demorar 25 minutos y se deberá guardar en una variable el número de Pomodoros
que vamos realizando (variable pomodoro:  pomodoros_realizados)
. Ya que al realizar 3 Pomodoros, el descanso se actualiza de 5 a 30 minutos

Luego nos preguntará nuevamente si queremos iniciar los 5 minutos de descanso. Tenemos que tener un iniciador
una letra o algo que debamos apretar para iniciarlo. De preferencia tambien vamos a ir guardando en una
variable la cantidad de descansos(Una vabiable: descanso_5 y otra descanso_30)

Si el usuario presiona opción 4 para terminar el programa. El mismo deberá mostrar al usuario cuantos pomodos realizó y cuantos descanso realizó de 5 y de 30 minutos.
"""


# Inicio del programa
pomodoro_contador = 0
descanso_5_contador = 0
descanso_30_contador = 0
while True:
    try:
        print("---- PRESIONA 1 PARA INICIAR UN POMODORO ----")
        print("---- PRESIONA 2 PARA INICIAR UN DESCANSO ----")
        print("---- PRESIONA 3 PARA MOSTRAR LOS POMODOROS ----")
        print("---- PRESIONA 4 PARA FINALIZAR EL PROGRAMA ----")
        
        opcion_usuario = int(input("Escribe tu opción: "))

        # Condicion 3 Pomodoros = Descanso de 30 minutos
        
        # [ OPCION 1 ]
        if opcion_usuario == 1:
            time.sleep(10) # 25 minutos = 1500 segundos
            print("Finalizó el Pomodoro")
            pomodoro_contador += 1

        # ---------------------------------------------------
        # [ OPCION 2 ]
        elif opcion_usuario == 2:
            
            if pomodoro_contador == 3:
                time.sleep(10) # 30 minutos = 1800 segundos
                print("Finalizó el descando de 30 minutos")
                
            time.sleep(10) # 5 minutos = 300 segundos
            descanso_5_contador += 1
        # ----------------------------------------------------
        # [ OPCION 3 ]
        elif opcion_usuario == 3:
            print("")
        # ----------------------------------------------------
        # [ OPCION 4 ]
        elif opcion_usuario == 4:
            print("Programa terminado")
            print("Los Pomodoros completados son:",pomodoro_contador)
            break
        else:
            print("Debe presionar una opción válida")
    except:
        print("EXCEPCION")