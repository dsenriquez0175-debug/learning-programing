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