import math
import bot as b

board = [["", "",  ""], 
         ["", "", ""],
         ["", "", ""]]

def draw_board():
    for y in range(3):
        row = ""
        for x in range(3):
            symbol = board[y][x]

            if symbol != "":
                row += symbol + "|"
            else:
                row += " |"
        print(row[:-1])
        if y != 2:
            print("-"*5)

def bot_input():
    bot = int(b.pick())

    bot_row, bot_col = position(bot)

    while board[bot_row][bot_col] != "":
        bot_row, bot_col = rechoose()
    
    b.data.remove(str(bot))
    b.used.append(str(bot))

    return (bot_row, bot_col)

def rechoose():
    bot = int(b.pick())

    bot_row, bot_col = position(bot)

    while board[bot_row][bot_col] != "":
        bot_row, bot_col = rechoose()
    
    return (bot_row, bot_col)

def player_input():
    player = int(input("1-9: "))

    while player < 1 or player > 9:
        player = int(input("1-9: "))

    return position(player)

def position(num):
    return (math.floor(num / 3.1), num % 3 - 1)

def win():
    #horizontals
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != "":
        return True
    elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != "":
        return True
    elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != "":
        return True
    
    #verticals
    elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != "":
        return True
    elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != "":
        return True
    elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != "":
        return True
    
    #diagonals
    elif board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return True
    elif board[2][0] == board[1][1] == board[0][2] and board[2][0] != "":
        return True
    
    else:
        return False

def draw():
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "":
                return False
    
    return True