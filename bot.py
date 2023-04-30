import random as r

f = open("D:\Codes\Python\Tic Tac Toe Bot\\bot_data.txt", "r")
data = f.readline().split(",")
f.close()

used = []

def pick():
    bot = r.choice(data)

    return bot