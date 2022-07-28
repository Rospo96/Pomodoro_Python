import funcion_descanso_5_min
import funcion_descanso_30_min
import funcion_pomodoro_25_min


# Inicio del programa
pomodoro_contador = 0
descanso_5_contador = 0
descanso_30_contador = 0
while True:
    try:
        print("---- PRESIONA 1 PARA INICIAR UN POMODORO ----")
        print("---- PRESIONA 2 PARA INICIAR UN DESCANSO ----")
        print("---- PRESIONA 3 PARA MOSTRAR LOS POMODOROS Y DESCANSOS ----")
        print("---- PRESIONA 4 PARA FINALIZAR EL PROGRAMA ----")
        
        opcion_usuario = int(input("Escribe tu opción: "))

        
        # [ OPCION 1 ]
        if opcion_usuario == 1:
            funcion_pomodoro_25_min.pomodoro_25()
            print("Finalizó el Pomodoro")
            pomodoro_contador += 1

        # ---------------------------------------------------
        # [ OPCION 2 ]
        elif opcion_usuario == 2:
            
            if pomodoro_contador == 3:
                funcion_descanso_30_min.descanso_30()
                descanso_30_contador += 1
                print("Finalizó el descando de 30 minutos")
                
            funcion_descanso_5_min.descanso_5()
            descanso_5_contador += 1
        # ----------------------------------------------------
        # [ OPCION 3 ]
        elif opcion_usuario == 3:
            print(f"Usted lleva {pomodoro_contador} Pomodoros")
            print(f"Usted lleva {descanso_5_contador} Descansos de 5 minutos")
            print(f"Usted lleva {descanso_30_contador} Descansos de 30 minutos")
        # ----------------------------------------------------
        # [ OPCION 4 ]
        elif opcion_usuario == 4:
            print("Programa terminado")
            print("Los Pomodoros completados son:",pomodoro_contador)
            print("Los Descansos de 5 minutos tomados son:",descanso_5_contador)
            print("Los Descansos de 30 minutos tomados son:",descanso_30_contador)
            break
        else:
            print("Debe presionar una opción válida")
    except:
        print("EXCEPCION")