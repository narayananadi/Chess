# ..................................reset board..............................#

def reset(tempboard):
    for x in range(8):
        setplayer(tempboard, 6, x, "white", "pawn")
        setplayer(tempboard, 1, x, "black", "pawn")
    setplayer(tempboard, 0, 0, "black", "rook")
    setplayer(tempboard, 0, 7, "black", "rook")
    setplayer(tempboard, 0, 1, "black", "knight")
    setplayer(tempboard, 0, 6, "black", "knight")
    setplayer(tempboard, 0, 2, "black", "bishop")
    setplayer(tempboard, 0, 5, "black", "bishop")
    setplayer(tempboard, 0, 3, "black", "queen")
    setplayer(tempboard, 0, 4, "black", "king")
    setplayer(tempboard, 7, 0, "white", "rook")
    setplayer(tempboard, 7, 7, "white", "rook")
    setplayer(tempboard, 7, 1, "white", "knight")
    setplayer(tempboard, 7, 6, "white", "knight")
    setplayer(tempboard, 7, 2, "white", "bishop")
    setplayer(tempboard, 7, 5, "white", "bishop")
    setplayer(tempboard, 7, 4, "white", "queen")
    setplayer(tempboard, 7, 3, "white", "king")
    return tempboard


# ..............................logic of pawn...................................#


def pawn(pos, tempi, tempj, player):
    possiblemoves = []
    if player == "black":
        if tempi - 1 >= 0 and pos[tempi - 1][tempj] == "null":
            possiblemoves.append([tempi - 1, tempj])
        if tempi - 1 >= 0 and tempj - 1 >= 0 and pos[tempi - 1][tempj - 1] != "null" and \
                pos[tempi - 1][tempj - 1].split(" ")[0] != player:
            possiblemoves.append([tempi - 1, tempj - 1])
        if tempi - 1 >= 0 and tempj + 1 <= 7 and pos[tempi - 1][tempj + 1] != "null" and \
                pos[tempi - 1][tempj + 1].split(" ")[0] != player:
            possiblemoves.append([tempi - 1, tempj + 1])
        if tempi == 6 and pos[5][tempj] == "null" and pos[4][tempj] == "null":
            possiblemoves.append([4, tempj])

    if player == "white":
        if tempi + 1 <= 7 and pos[tempi + 1][tempj] == "null":
            possiblemoves.append([tempi + 1, tempj])
        if tempi + 1 <= 7 and tempj - 1 >= 0 and pos[tempi + 1][tempj - 1] != "null" and \
                pos[tempi + 1][tempj - 1].split(" ")[0] != player:
            possiblemoves.append([tempi + 1, tempj - 1])
        if tempi + 1 <= 7 and tempj + 1 <= 7 and pos[tempi + 1][tempj + 1] != "null" and \
                pos[tempi + 1][tempj + 1].split(" ")[0] != player:
            possiblemoves.append([tempi + 1, tempj + 1])
        if tempi == 1 and pos[3][tempj] == "null" and pos[2][tempj] == "null":
            possiblemoves.append([3, tempj])

    return possiblemoves


# ..................................logic of rook..............................#


def rook(pos, tempi, tempj, player):
    possiblemoves = []
    upper = 8
    lower = -1
    left = -1
    right = 8
    for x in range(tempi + 1, 8):
        if pos[x][tempj] != "null":
            upper = x
            if pos[x][tempj].split(" ")[0] != player:
                print("upper")
                possiblemoves.append([x, tempj])
            break

    for x in range(tempi - 1, -1, -1):
        if pos[x][tempj] != "null":
            lower = x
            if pos[x][tempj].split(" ")[0] != player:
                print("lower")
                possiblemoves.append([x, tempj])
            break

    for x in range(tempi + 1, upper):
        if pos[x][tempj] == "null":
            possiblemoves.append([x, tempj])

    for x in range(tempi - 1, lower, -1):
        if pos[x][tempj] == "null":
            possiblemoves.append([x, tempj])

    for x in range(tempj + 1, 8):
        if pos[tempi][x] != "null":
            right = x
            print("right")
            if pos[tempi][x].split(" ")[0] != player:
                possiblemoves.append([tempi, x])
            break

    for x in range(tempj - 1, -1, -1):
        if pos[tempi][x] != "null":
            left = x
            if pos[tempi][x].split(" ")[0] != player:
                print("left")
                possiblemoves.append([tempi, x])
            break

    for x in range(tempj + 1, right):
        if pos[tempi][x] == "null":
            possiblemoves.append([tempi, x])

    for x in range(tempj - 1, left, -1):
        if pos[tempi][x] == "null":
            possiblemoves.append([tempi, x])
    return possiblemoves


# ........................knight.................#

def knight(pos, tempi, tempj, player):
    possiblemoves = []
    if tempi - 1 >= 0 and tempj - 2 >= 0 and pos[tempi - 1][tempj - 2].split(" ")[0] != player:
        possiblemoves.append([tempi - 1, tempj - 2])
    if tempi - 2 >= 0 and tempj - 1 >= 0 and pos[tempi - 2][tempj - 1].split(" ")[0] != player:
        possiblemoves.append([tempi - 2, tempj - 1])
    if tempi - 2 >= 0 and tempj + 1 <= 7 and pos[tempi - 2][tempj + 1].split(" ")[0] != player:
        possiblemoves.append([tempi - 2, tempj + 1])
    if tempi - 1 >= 0 and tempj + 2 <= 7 and pos[tempi - 1][tempj + 2].split(" ")[0] != player:
        possiblemoves.append([tempi - 1, tempj + 2])
    if tempi + 1 <= 7 and tempj + 2 <= 7 and pos[tempi + 1][tempj + 2].split(" ")[0] != player:
        possiblemoves.append([tempi + 1, tempj + 2])
    if tempi + 2 <= 7 and tempj + 1 <= 7 and pos[tempi + 2][tempj + 1].split(" ")[0] != player:
        possiblemoves.append([tempi + 2, tempj + 1])
    if tempi + 2 <= 7 and tempj - 1 >= 0 and pos[tempi + 2][tempj - 1].split(" ")[0] != player:
        possiblemoves.append([tempi + 2, tempj - 1])
    if tempi + 1 <= 7 and tempj - 2 >= 0 and pos[tempi + 1][tempj - 1].split(" ")[0] != player:
        possiblemoves.append([tempi + 1, tempj - 2])

    return possiblemoves


# .......................bhishop.....................................#

def bishop(pos, tempi, tempj, player):
    possiblemoves = []
    # upper left quadrant
    x = tempi - 1
    y = tempj - 1
    while True:
        if x < 0 or y < 0:
            break
        if pos[x][y] == "null":
            possiblemoves.append([x, y])
        if pos[x][y] != "null" and pos[x][y].split(" ")[0] != player:
            possiblemoves.append([x, y])
            break
        if pos[x][y].split(" ")[0] == player:
            break
        y -= 1
        x -= 1

    # lower right quadrant
    x = tempi + 1
    y = tempj + 1
    while True:
        if x > 7 or y > 7:
            break
        if pos[x][y] == "null":
            possiblemoves.append([x, y])

        if pos[x][y] != "null" and pos[x][y].split(" ")[0] != player:
            possiblemoves.append([x, y])
            break
        y += 1
        x += 1

    # upper right quarant
    x = tempi - 1
    y = tempj + 1
    while True:
        if x < 0 or y > 7:
            break
        if pos[x][y] == "null":
            possiblemoves.append([x, y])

        if pos[x][y] != "null" and pos[x][y].split(" ")[0] != player:
            possiblemoves.append([x, y])
            break
        y += 1
        x -= 1

    # left lower quarant
    x = tempi + 1
    y = tempj - 1

    while True:
        if x > 7 or y < 0:
            break
        if pos[x][y] == "null":
            possiblemoves.append([x, y])

        if pos[x][y] != "null" and pos[x][y].split(" ")[0] != player:
            possiblemoves.append([x, y])
            break
        y -= 1
        x += 1

    return possiblemoves


# ......................set starting peice position(debug)........................#


def setplayer(pos, i, j, templayer, tempentity):
    pos[i][j] = templayer + " " + tempentity


# ..............................set peice position................................#
# def setplayer(prevtempi, prevtempj, pos, i, j, templayer, tempentity):
#     pos[i][j] = templayer + " " + tempentity
#     pos[prevtempi][prevtempj] = "null"

# ...................print board...................................#


def printboard(pos):
    x = 0
    y = 0
    while x < 8:
        y = 0
        while y < 8:
            print(pos[x][y] + "[" + str(x) + "][" + str(y) + "] ", end=" | ")
            y += 1
        print(end="\n")
        x += 1
    print(end="\n \n")


# ...................................debug................................#


def selectpiece():
    print("choose peice position")
    piece1 = int(input())
    piece2 = int(input())


if __name__ == '__main__':
    board = [["null"] * 8 for _ in range(8)]
    printboard(board)
    setplayer(board, 4, 4, "black", "bishop")
    setplayer(board, 6, 2, "black", "bishop")
    setplayer(board, 2, 6, "white", "bishop")
    printboard(board)
    print(bishop(board, 4, 4, "black"))
