# 6. Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos
# de un dia desde las 00:00:00 horas hasta las 23:59:59 horas.

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

# Inicio variables hora, minutos, segundos.
h= 0
m = 0
s = 0

# Mostrar en pantalla.
print('\n##### EJERCICIO 06 #####\n')

# Inicio ciclos.
while h < 24:
    while m < 60:
        while s < 60:
                
            h_str = str(h)
            if h < 10:
                h_str = '0' + h_str
                  
            m_str = str(m)
            if m < 10:
                m_str = '0' + m_str

            s_str = str(s)
            if s < 10:
                s_str = '0' + s_str

            print(h_str + ':' + m_str + ':' + s_str)

            # Incrementa los segundos en 1.
            s += 1
        # Incrementa los minutos en 1 y resetea los segundos.
        m += 1
        s = 0
    # Incrementa las horas en 1 y resetea los minutos.
    h += 1
    m = 0

print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#