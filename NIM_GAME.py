#This game is played by removing 1 or 2 stones from a pile of 20 stones.
#Player who takes the last stone is the loser.

def main():
    PLAYER_TURN = 2
    stones = 20

    while stones != 0:
        print(f"There are {stones} stones left")
        msg1a = "Player 1 would you like to remove 1 or 2 stones? "
        msg2a = "Player 2 would you like to remove 1 or 2 stones? "
        msg3 = "Please enter 1 or 2: "

        #PLAYER 1
        if PLAYER_TURN % 2 == 0:
            take = input(msg1a)
            take = int(take)
            if take > 2:
                take = input(msg3)
                take = int(take)
            elif take < 1:
                take = input(msg3)
                take = int(take)
            PLAYER_TURN += 1
            print("")

        #PLAYER 2
        elif PLAYER_TURN % 2 == 1:
            take = input(msg2a)
            take = int(take)
            if take > 2:
                take = input(msg3)
                take = int(take)
            elif take < 1:
                take = input(msg3)
                take = int(take)
            PLAYER_TURN += 1
            print("")

        if take < 3 :
            stones -= take
        else:
            print("You've done did it now!\nArrivederci!")
            break


    if stones == 0:
        if PLAYER_TURN % 2 == 1:
            print("Player 2 wins!")
        elif PLAYER_TURN % 2 == 0:
            print("Player 1 wins!")

if __name__ == '__main__':
    main()