# game_logic.py · traduce DF2 (validación de la jugada) · RF-03, RF-04, RF-05, RF-06, RF-07, RF-08

t = [""] * 10
i = 1

for x in range(9):
    t[i] = " "
    i = i + 1

jugadas = 0
gana = 0
turno = "X"
jugador1 = "ju1"
jugador2 = "ju2"

while gana != 1 and jugadas != 9:  # RF-06, RF-08
    casilla_valida = False

    while not casilla_valida:
        numero = False

        while not numero:
            casilla = input("Ingrese una casilla de (1-9): ")  # RF-05
            if casilla.isdigit():
                casilla = int(casilla)
                numero = True
            else:
                print("Ingrese un número")

        if casilla >= 1 and casilla <= 9 and t[casilla] == " ":
            casilla_valida = True
        else:
            print("La casilla esta ocupada o fuera de rango")

    t[casilla] = turno
    y = input(
        "Escriba 1 para que gane el jugador1, 2 para que gane el jugador2 o 0 para seguir jugando(esta parte se evalua en base al juego): "
    )  # RF-04

    y = int(y)

    if y == 1:
        gana = 1
        actual = jugador1
    elif y == 2:
        gana = 1
        actual = jugador2

    if gana == 0:
        if turno == "X":
            turno = "O"
            actual = jugador2
        else:
            turno = "X"
            actual = jugador1

        jugadas = jugadas + 1

    print(t[1] + "|" + t[2] + "|" + t[3])  # RF-03
    print(t[4] + "|" + t[5] + "|" + t[6])
    print(t[7] + "|" + t[8] + "|" + t[9])

if gana == 1:  # RF-07, RF-08
    print("Gana " + actual)
else:
    print("Empate")
