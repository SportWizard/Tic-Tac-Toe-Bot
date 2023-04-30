import tic_tac_toe as t
import bot as b
import bot_data_update as bdu

def main():
    #bot
    bot_row, bot_col = t.bot_input()

    t.board[bot_row][bot_col] = "o"

    t.draw_board()
    print("")

    winner = t.win()

    if winner == True:
        print("Bot Wins")
        bdu.update("bot wins")
        exit()
    
    draw = t.draw()

    if draw == True:
        print("Draw")
        bdu.update("draw")
        exit()

    #player
    player_row, player_col = t.player_input()

    while t.board[player_row][player_col] != "":
        player_row, player_col = t.player_input()

    t.board[player_row][player_col] = "x"

    t.draw_board()
    print("")

    winner = t.win()

    if winner == True:
        print("Player Wins")
        bdu.update("player wins")
        exit()

    draw = t.draw()

    if draw == True:
        print("Draw")
        bdu.update("draw")
        exit()

if __name__ == '__main__':
    while True:
        main()