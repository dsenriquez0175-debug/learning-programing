# Import packges
import random randint

# functions
def draw_dices():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return d1, d2, d1 + d2

def play():
    print(":::NUMERICAL RACE:::")
    N_jugadores = int(input("¿how many players? (2-4): "))
    print("1. principiante(20) 2. Intermedio(30) 3. avanzado(50) 4. Experto(100)")
    option = int(input("choose level (1-4): "))

# define goal according to the option

if potion == 1. meta = 20
elif option == 2. meta = 30
elif option == 3. meta = 50
else: meta = 100

# control variables
posiciones = [0] * N_jugadores
consecutivos = [0] * N_jugadores
hay_ganador = false

# 3. Ciclo principal del juego
while not hay_ganador:
     for i in range(n_jugadores):
        print(f"\nTurno Jugador {i+1}")
        input("Presiona Enter para lanzar...")
            
    d1, d2, suma = lanzar_dados()
    print(f"Dados: {d1} y {d2} (Suma: {suma})")

# Regla de los 3 pares consecutivos
if d1 == d2:
    consecutivos[i] += 1
    print(f"¡Llevas {consecutivos[i]} pares!")
else:
                consecutivos[i] = 0

            if consecutivos[i] == 3:
                print(f"¡EL JUGADOR {i+1} GANÓ POR TRIPLE PAR!")
                hay_ganador = True
                break

            # Movimiento normal
            posiciones[i] += suma
            print(f"Vas en la posición: {posiciones[i]}")

            if posiciones[i] >= meta:
                print(f"¡EL JUGADOR {i+1} GANÓ POR LLEGAR A LA META!")
                hay_ganador = True
                break

jugar() 