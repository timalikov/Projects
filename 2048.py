import random

def print_table(t):
    for i in t:
        print(i)

def generate_first_2(table):
    a, b = random.randint(0, 3), random.randint(0, 3)
    table[a][b] = 2
    a1, b1 = random.randint(0, 3), random.randint(0, 3)
    if a1 != a or b1 != b:
        table[a1][b1] = 2
    else:
        while a == a1 and b == b1:
            a1, b1 = random.randint(0, 3), random.randint(0, 3)
        table[a1][b1]


table = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

rows = range(4)

running = True
while running:
    generate_first_2(table)
    print_table(table)

    turn = input("Make your turn(w/a/s/d) or \"quit\" for quit: ")
    while turn != "quit":
        if turn == 'w':
            for i in range(1, 4):
                for j in range(4):
                    if table[i][j] != 0:
                        for up in range(0, i, -1):
                            if table[up][j] == table[i][j]:
                                table[i][j] = 0
                                table[up][j] *= 2
                            elif table[up][j] == 0:
                                table[up][j] = table[i][j] 
                                table[i][j] = 0
        print_table(table)
        turn = input("Make your turn(w/a/s/d) or \"quit\" for quit: ")


    break    