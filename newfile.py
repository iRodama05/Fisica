import math

def nivel_1():
    print(">> Nivel 1: Suelo con fricción simple\n")
    print("Meta: 5 metros, margen de error: ±0.25 m")
    print("Coeficiente de fricción (\u03BC): 0.3")
    print("Masa de la bola: 1 kg")
    
    # Constantes
    d = 5  # Distancia a la meta en metros
    mu = 0.3  # Coeficiente de fricción
    m = 1  # Masa de la bola en kg
    g = 9.81  # Gravedad
    
    # Calcular fuerza de fricción y trabajo necesario
    F_friccion = mu * m * g
    W = F_friccion * d  # Trabajo total
    v_requerida = math.sqrt(2 * W / m)  # Velocidad inicial requerida
    F_requerida = m * v_requerida**2 / (2 * d)  # Fuerza inicial requerida (simplificación)

    print(f"\nPara acertar, debes calcular la fuerza adecuada para mover la bola 5 metros. La fricción genera un "
          f"trabajo que debes superar.\n")
    
    # Entrada del jugador
    F_jugador = float(input("¿Con cuánta fuerza deseas golpear la bola? (en Newtons): "))
    
    # Evaluación
    E_jugador = F_jugador * d  # Energía generada por la fuerza del jugador
    v_jugador = math.sqrt(2 * E_jugador / m)  # Velocidad inicial generada
    d_real = (v_jugador**2) / (2 * (mu * g))  # Distancia recorrida
    
    if d - 0.25 <= d_real <= d + 0.25:
        print(f"¡Felicidades! La bola recorrió {d_real:.2f} metros y llegó a la meta.")
    elif d_real < d - 0.25:
        print(f"La bola recorrió {d_real:.2f} metros. Te quedaste corto.")
    else:
        print(f"La bola recorrió {d_real:.2f} metros. Te pasaste.")

def nivel_2():
    print("\nNivel 2: Cambio de fricción")
    print("Meta: 5 metros, margen de error: ±0.25 m")
    print("Primer tramo (0-2 m): Fricción (\u03BC1): 0.3")
    print("Segundo tramo (2-5 m): Fricción (\u03BC2): 0.6")
    print("Masa de la bola: 1 kg")
    
    # Constantes
    d1, d2 = 2, 3  # Distancias de los tramos
    mu1, mu2 = 0.3, 0.6  # Coeficientes de fricción
    m = 1  # Masa de la bola en kg
    g = 9.81  # Gravedad
    d = 5 # Distancia de la meta
    
    # Calcular fuerzas de fricción y trabajo necesario
    F1 = mu1 * m * g
    F2 = mu2 * m * g
    W = (F1 * d1) + (F2 * d2)  # Trabajo total
    v_requerida = math.sqrt(2 * W / m)  # Velocidad inicial requerida
    F_requerida = m * v_requerida**2 / (2 * (d1 + d2))  # Fuerza inicial requerida

    print(f"\nAhora hay dos tramos con distinta fricción. Calcula la fuerza adecuada para superar ambos.\n")
    
    # Entrada del jugador
    F_jugador = float(input("¿Con cuánta fuerza deseas golpear la bola? (en Newtons): "))
    
    # Evaluación
    E_jugador = F_jugador * (d1 + d2)  # Energía generada por la fuerza del jugador
    v_jugador = math.sqrt(2 * E_jugador / m)  # Velocidad inicial generada
    d_real1 = (v_jugador**2) / (2 * (mu1 * g))  # Distancia recorrida en el primer tramo
    
    if d_real1 > d1:  # Si recorre más del primer tramo
        v_resto = math.sqrt(v_jugador**2 - 2 * F1 * d1 / m)
        d_real2 = (v_resto**2) / (2 * (mu2 * g))
        d_total = d1 + d_real2
    else:
        d_total = d_real1
    
    if d - 0.25 <= d_total <= d + 0.25:
        print(f"¡Felicidades! La bola recorrió {d_total:.2f} metros y llegó a la meta.")
    elif d_total < d - 0.25:
        print(f"La bola recorrió {d_total:.2f} metros. Te quedaste corto.")
    else:
        print(f"La bola recorrió {d_total:.2f} metros. Te pasaste.")

def nivel_3():
    print("\nNivel 3: Resorte y puerta bloqueada")
    print("Meta: 5 metros a la derecha")
    print("Resorte: 2 metros a la izquierda (constante elástica k = 50 N/m)")
    print("La bola debe golpear el resorte y usar el impulso para alcanzar la meta.")
    
    # Constantes
    d_resorte = 2  # Distancia al resorte
    d_meta = 5  # Distancia a la meta desde el inicio
    k = 50  # Constante elástica del resorte (N/m)
    m = 1  # Masa de la bola (kg)
    g = 9.81  # Gravedad
    
    # Calcular fuerza necesaria para comprimir el resorte
    x_requerido = d_meta + d_resorte  # Distancia total requerida
    W_resorte = 0.5 * k * (x_requerido)**2  # Energía almacenada en el resorte
    v_requerida = math.sqrt(2 * W_resorte / m)  # Velocidad requerida para alcanzar la meta
    F_requerida = m * v_requerida**2 / (2 * d_resorte)  # Fuerza inicial
    
    print(f"\nDebes calcular la fuerza necesaria para comprimir el resorte y liberar la bola hacia la meta.\n")
    
    # Entrada del jugador
    F_jugador = float(input("¿Con cuánta fuerza deseas golpear la bola? (en Newtons): "))
    
    # Evaluación
    E_jugador = F_jugador * d_resorte  # Energía generada por la fuerza del jugador
    x_jugador = math.sqrt(2 * E_jugador / k)  # Compresión del resorte lograda
    W_jugador = 0.5 * k * x_jugador**2  # Energía almacenada en el resorte
    v_jugador = math.sqrt(2 * W_jugador / m)  # Velocidad inicial generada
    
    if abs(v_jugador - v_requerida) < 0.5:
        print(f"¡Felicidades! La bola alcanzó la meta correctamente.")
    elif v_jugador < v_requerida:
        print(f"La bola no alcanzó la meta. Le faltó impulso.")
    else:
        print(f"La bola sobrepasó la meta.")

def nivel_4():
    print("\nNivel 4: Botón en la pared")
    print("Meta: 5 metros a la derecha")
    print("Botón: 6 metros a la derecha (rebote necesario)")
    print("Coeficiente de restitución del rebote: 0.8")
    
    # Constantes
    d_meta = 5  # Distancia a la meta desde el inicio
    d_boton = 6  # Distancia al botón desde el inicio
    e = 0.8  # Coeficiente de restitución (rebote)
    m = 1  # Masa de la bola (kg)
    g = 9.81  # Gravedad
    mu = 0.3  # Fricción en el suelo
    
    # Calcular fuerza necesaria para alcanzar el botón y rebotar
    W_boton = mu * m * g * d_boton  # Trabajo para alcanzar el botón
    v_boton = math.sqrt(2 * W_boton / m)  # Velocidad inicial necesaria
    v_rebote = e * v_boton  # Velocidad después del rebote
    W_rebote = 0.5 * m * v_rebote**2  # Energía restante tras el rebote
    d_rebote = W_rebote / (mu * g)  # Distancia recorrida tras el rebote
    F_requerida = m * v_boton**2 / (2 * d_boton)  # Fuerza inicial
    
    print(f"\nDebes calcular la fuerza necesaria para que la bola golpee el botón y rebote hasta la meta.\n")
    
    # Entrada del jugador
    F_jugador = float(input("¿Con cuánta fuerza deseas golpear la bola? (en Newtons): "))
    
    # Evaluación
    E_jugador = F_jugador * d_boton  # Energía generada por la fuerza del jugador
    v_jugador = math.sqrt(2 * E_jugador / m)  # Velocidad inicial generada
    v_rebote_jugador = e * v_jugador  # Velocidad tras el rebote
    d_rebote_jugador = (v_rebote_jugador**2) / (2 * (mu * g))  # Distancia tras el rebote
    
    if abs(d_meta - d_rebote_jugador) <= 0.25:
        print(f"¡Felicidades! La bola alcanzó el botón y rebotó hasta la meta.")
    elif d_rebote_jugador < d_meta:
        print(f"La bola no llegó a la meta tras el rebote. Se quedó corta.")
    else:
        print(f"La bola rebotó demasiado lejos de la meta.")

def nivel_5():
    print("\nNivel 5: Bloque de madera frente a la meta")
    print("Meta: 5 metros")
    print("Bloque de madera: 500 g (Coeficiente de fricción: 0.4)")
    
    # Constantes
    d_meta = 5  # Distancia a la meta desde el inicio
    m_bola = 1  # Masa de la bola (kg)
    m_bloque = 0.5  # Masa del bloque (kg)
    mu = 0.4  # Coeficiente de fricción del bloque
    g = 9.81  # Gravedad
    
    # Calcular fuerza necesaria para mover el bloque
    F_friccion_bloque = mu * m_bloque * g
    W_bloque = F_friccion_bloque * d_meta  # Trabajo necesario para mover el bloque
    v_requerida = math.sqrt(2 * W_bloque / m_bola)  # Velocidad requerida
    F_requerida = m_bola * v_requerida**2 / (2 * d_meta)  # Fuerza inicial requerida
    
    print(f"\nDebes calcular la fuerza necesaria para que la bola empuje el bloque hasta la meta.\n")
    
    # Entrada del jugador
    F_jugador = float(input("¿Con cuánta fuerza deseas golpear la bola? (en Newtons): "))
    
    # Evaluación
    E_jugador = F_jugador * d_meta  # Energía generada por la fuerza del jugador
    v_jugador = math.sqrt(2 * E_jugador / m_bola)  # Velocidad inicial generada
    W_jugador = 0.5 * m_bola * v_jugador**2  # Energía inicial generada
    d_bloque = W_jugador / F_friccion_bloque  # Distancia recorrida por el bloque
    
    if abs(d_meta - d_bloque) <= 0.25:
        print(f"¡Felicidades! La bola empujó el bloque y alcanzó la meta.")
    elif d_bloque < d_meta:
        print(f"La bola no logró empujar el bloque hasta la meta. Se quedó corta.")
    else:
        print(f"La bola empujó el bloque demasiado lejos de la meta.")


# Ejecución del juego
print("¡Bienvenido al juego de Física basado en texto!\n")
nivel_1()
nivel_2()
nivel_3()
nivel_4()
nivel_5()