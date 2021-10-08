import sys
import utilities.logic as lg

def win():
    if lg.player_score == 2:
        print("El jugador gana el juego")
        print(f"El resultado final ha sido Jugador {lg.player_score} - {lg.computer_score} Ordenador")
        sys.exit()
    if lg.computer_score == 2:
        print ("Te he ganado, gracias por jugar")
        print(f"El resultado final ha sido Jugador {lg.player_score} - {lg.computer_score} Ordenador")
        
        sys.exit()
    