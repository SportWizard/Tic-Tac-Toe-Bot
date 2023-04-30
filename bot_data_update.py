import bot as b

def update(winner):
    data = b.data
    used = b.used

    if winner == "bot wins":
        for i in used:
            for m in range(3):
                data.append(i)
    elif winner == "draw":
        for i in used:
            for m in range(2):
                data.append(i)

    data_string = ""

    for n in data:
        data_string += n + ","
    
    f = open("D:\Codes\Python\Tic Tac Toe Bot\\bot_data.txt", "w")
    f.write(data_string[:-1])
    f.close()