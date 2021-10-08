"""
Rock Paper Scissor Terminal Game

Author: Enrique Revuelta
Date: 7th October 2021
"""
import sys
import utilities.logic as lg

# With this command iniciate the program
if __name__ == "__main__":
    print("****   ****    ****")
    print("*   *  *   *  *    *")
    print("****   ****    *")
    print("*   *  *         *  ")
    print("*   *  *      *    * ")
    print("*   *  *       ****")
    # With this sentence set the choice value taking it by terminal argv
    lg.choice = sys.argv[1]
    # Execute the game with the choice value
    lg.rps_game(lg.choice)
