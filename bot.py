import random as r

f = open("bot_data.txt", "r")
data = f.readline().split(",")
f.close()

used = []

def pick():
    bot = r.choice(data)

    return bot