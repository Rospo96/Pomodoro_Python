import time

def pomodoro_25():
    minutos = 0
    segundos = 0
    segundos_60 = 60
    
    while True:
        if minutos == 2:
            print(f"Finalizó un Pomodoro: {minutos} minutos : {segundos} segundos")
            break
                    
        
        if segundos <= 59:
            segundos += 1
            time.sleep(1)
            print(minutos,":",segundos)
        
    
        elif segundos == segundos_60:
            minutos += 1        
            segundos = 0                    
            time.sleep(1)
            print(minutos,":",segundos)
        
