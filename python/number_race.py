# Import packges
import random randint

# functions
def draw_dices():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    return d1, d2, d1 + d2

def play():
    print(":::NUMERICAL RACE:::")
    while true:
        N_jugadores = int(imput("¿How many players? (2-4): "))
        if 2 <= N_jugadores <=4:
            break
        print("Error: there must be between 2 and 4 players")
    print("\n1. principiante (20)")
    print("2. Intermedio (30)")
    print("3. Avanzado (50)")
    print("4. Experto (100)")
    option = int(input("choose level (1-4): "))

# Validate level

if option == 1. meta = 20
elif option == 2. meta = 30
elif option == 3. meta = 50
elif: meta = 100
else:
    print("Invalid level")

# control variables
posiciones = [0] * N_jugadores
consecutivos = [0] * N_jugadores
hay_ganador = false

print(f"\nThe is the position {meta}")

    # 3. main cycle 
    while not hay_ganador:
        for i in range(N_jugadores):
            print(f"\nTurno Jugador {i+1}")
            input("press enter to launch:::")
            
            d1, d2, suma = lanzar_dados()
            print(f"Dados: {d1} y {d2} (Suma: {suma})")

            # rule 3 consecutive pairs
            if d1 == d2:
                consecutivos[i] += 1
                print(f"¡you carry {consecutivos[i]} pairs!")
            else:
                consecutivos[i] = 0

            if consecutivos[i] == 3:
                print(f"¡THE PLAYER{i+1} WON BY TRYPLE PAIR!")
                hay_ganador = True
                break

            # Normal movement
            posiciones[i] += suma
            print(f"you are in the position: {posiciones[i]}")

            if posiciones[i] >= meta:
                print(f"¡THE PLAYER{i+1} WON BY TRYPLE PAIR!")
                hay_ganador = True
                break

play() 