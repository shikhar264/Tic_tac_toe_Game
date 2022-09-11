pattern = "         "
print("---------")
print("| " + pattern[0] + " " + pattern[1] + " " + pattern[2] + " |")
print("| " + pattern[3] + " " + pattern[4] + " " + pattern[5] + " |")
print("| " + pattern[6] + " " + pattern[7] + " " + pattern[8] + " |")
print("---------")
M = [[pattern[0],pattern[1],pattern[2]],[pattern[3],pattern[4],pattern[5]],[pattern[6],pattern[7],pattern[8]]]
a = []
x = 1
temp = 0
is_any_underscore = True
for i in range(len(M)):
    for j in range(3):
        a.append(M[i][j])
while is_any_underscore:
    p = 0
    q = 0
    r= 0
    s = 0
    for i in range(len(a)):
        if a[i] == "X":
            p += 1
        elif a[i] == "O":
            q += 1
    if a[0] == a[1] == a[2] == "X" or a[1] == a[4] == a[7] == "X" or a[3] == a[4] == a[5] == "X" or a[0] == a[3] == a[6] == "X" or a[2] == a[5] == a[8] == "X"  or a[6] == a[7] == a[8] == "X" or a[2] == a[4] == a[6] == "X" or a[0] == a[4] == a[8] == "X":
        if p == q + 1 or q == p + 1 or p == q:
            r += 1
    if a[0] == a[1] == a[2] == "O" or a[1] == a[4] == a[7] == "O" or a[3] == a[4] == a[5] == "O" or a[0] == a[3] == a[6] == "O" or a[2] == a[5] == a[8] == "O"  or a[6] == a[7] == a[8] == "O" or a[2] == a[4] == a[6] == "O" or a[0] == a[4] == a[8] == "O":
        if p == q + 1 or q == p + 1 or p == q:
            s += 1
    if r > s:
        print("X wins")
        exit()
    elif s > r:
        print("O wins")
        exit()
    if temp == 1:
         print("Draw")
         exit()

        
    

    i, j = input().split()
    if i.isdigit() and j.isdigit():
        i = int(i) - 1
        j = int(j) - 1
    else:
        print("You should enter numbers!")
    if i >= len(M) or j >= len(M):
        print("Coordinates should be from 1 to 3!")
    elif M[i][j] != " ":
        print("This cell is occupied! Choose another one!")
    else:
        if x % 2 != 0:
            M[i][j] = 'X'
        else:
            M[i][j] = 'O'
        x += 1
        a.clear()
        for i in range(3):
            for j in range(3):
                a.append(M[i][j]) 
        print("---------")
        print("| " + a[0] + " " + a[1] + " " + a[2] + " |")
        print("| " + a[3] + " " + a[4] + " " + a[5] + " |")
        print("| " + a[6] + " " + a[7] + " " + a[8] + " |")
        print("---------")
    
    if ' ' not in a :
        temp = 1
        is_any_underscore = True
