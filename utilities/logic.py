"""
This file determine the logic of the Game
"""
import random
import utilities.win as win

computer_ia = {
    "0": "pi",
    "1": "pa",
    "2": "ti"
}

player_score = 0
computer_score = 0
choice = ""

def rps_game(choice):
    global player_score
    global computer_score
    c_ia = computer_ia[str(random.randint(0,2))]
    if choice != "pi" and choice != "pa" and choice != "ti":
        print("Elige una opción correcta")
        print("pi = Piedra")
        print("pa = Papel")
        print("ti = Tijeras")
        choice = str(input("Introduce tu opción, Piedra, Papel o Tijera:"))
        rps_game(choice)
    else:
        if choice == c_ia:
            print(f"Elegiste {choice} y el ordenador eligió {c_ia}")
            print("EMPATE!!!")
            print("Teneis que volver a jugar...")
            choice = str(input("Introduce tu opción, Piedra, Papel o Tijera:"))
            rps_game(choice)
        elif choice == "pi" and c_ia == "ti":
            print("Piedra gana a Tijera")
            print("Ganaste")
            player_score += 1
            win.win()
            print("Juguemos al mejor de 3 :)")
            choice = str(input("Introduce tu opción, Piedra, Papel o Tijera:"))
            rps_game(choice)
            
            
        elif choice == "pi" and c_ia == "pa":
            print("Papel gana a Piedra")
            print("Gano yo ;)")
            computer_score += 1
            win.win()
            print("Juguemos al mejor de 3 :)")
            choice = str(input("Introduce tu opción, Piedra, Papel o Tijera:"))
            rps_game(choice)
           
            
        elif choice == "pa" and c_ia == "ti":
            print("Tijera gana a Papel")
            print("Gano yo ;)")
            computer_score += 1
            win.win()
            print("Juguemos al mejor de 3 :)")
            choice = str(input("Introduce tu opción, Piedra, Papel o Tijera:"))
            rps_game(choice)
            
        
        elif choice == "pa" and c_ia == "pi":
            print("Papel gana a Piedra")
            print("Ganaste")
            player_score += 1
            win.win()
            print("Juguemos al mejor de 3 :)")
            choice = str(input("Introduce tu opción, Piedra, Papel o Tijera:"))
            rps_game(choice)
            
        
        elif choice == "ti" and c_ia == "pa":
            print("Tijera gana a Papel")
            print("Ganaste")
            player_score += 1
            win.win()
            print("Juguemos al mejor de 3 :)")
            choice = str(input("Introduce tu opción, Piedra, Papel o Tijera:"))
            rps_game(choice)
            
            
        elif choice == "ti" and c_ia == "pi":
            print("Piedra gana a Tijera")
            print("Gano yo ;)")
            computer_score += 1
            win.win()
            print("Juguemos al mejor de 3 :)")
            choice = str(input("Introduce tu opción, Piedra, Papel o Tijera:"))
            rps_game(choice)
            
        
        else:
            pass
            