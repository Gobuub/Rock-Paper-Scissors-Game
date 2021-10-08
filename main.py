"""
Rock Paper Scissor Terminal Game

Author: Enrique Revuelta
Date: 7th October 2021
"""
import sys
import utilities.logic as lg

# With this command iniciate the program
if __name__ == "__main__":
    # With this sentence set the choice value taking it by terminal argv
    if sys.argv[1] == "":
        print("Escoje una opción.")
        print("pi = Piedra")
        print("pa = Papel")
        print("ti = Tijeras")
        print(str(input("Introduce tu opción:")))
    else:
        lg.choice = sys.argv[1]
    # Execute the game with the choice value
    lg.rps_game(lg.choice)