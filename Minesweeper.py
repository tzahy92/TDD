from enum import Enum


class GameStatus(Enum):
    PLAYING = 0
    WIN = 1
    LOST = 2

class minesweeper:
    def __init__(self):
        self.row = 0
        self.col = 0
        self.miner = []
        self.stat = GameStatus
        self.showIndexs = []
        self.countMins = 0

    def crratField(self, row, col):
        if (row <= 0 or col <= 0):
            return False
        self.row = row
        self.col = col
        self.miner = [[0 for x in range(col)] for y in range(row)]
        return True

    def layMine(self, row, col):
        if ((row < 0 or row >= self.row) or (col < 0 or col >= self.col)):
            assert IndexError("the row or col is out of range")
        if (self.miner[row][col] == '*'):
            print("you already lay min in row: ", row, "col: ", col)
            return
        self.miner[row][col] = '*'
        self.countMins += 1
        if (row - 1 >= 0):
            if (col - 1 >= 0 and self.miner[row - 1][col - 1] != '*'):
                self.miner[row - 1][col - 1] += 1
            if (self.miner[row - 1][col] != '*'):
                self.miner[row - 1][col] += 1
            if (col + 1 < self.col and self.miner[row - 1][col + 1] != '*'):
                self.miner[row - 1][col + 1] += 1
        if (col - 1 >= 0 and self.miner[row][col - 1] != '*'):
            self.miner[row][col - 1] += 1
        if (col + 1 < self.col and self.miner[row][col + 1] != '*'):
            self.miner[row][col + 1] += 1
        if (row + 1 < self.row):
            if (col - 1 >= 0 and self.miner[row + 1][col - 1] != '*'):
                self.miner[row + 1][col - 1] += 1
            if (self.miner[row + 1][col] != '*'):
                self.miner[row + 1][col] += 1
            if (col + 1 < self.col and self.miner[row + 1][col + 1] != '*'):
                self.miner[row + 1][col + 1] += 1

    def play(self, row, col):
        if self.stat == GameStatus:
            self.stat = GameStatus.PLAYING
        if row < 0 or col < 0 or row >= self.row or col >= self.col:
            assert IndexError("the row or col is out of range")
        if self.miner[row][col] == '*':
            self.stat = GameStatus.LOST
            return
        def floodfill(matrix, row, col):
            if matrix[row][col] == 0:
                if [row,col] not in self.showIndexs:
                    self.showIndexs += [[row,col]]
                matrix[row][col] = '+'
                if row > 0:
                    floodfill(matrix, row - 1, col)
                if row < len(matrix) - 1:
                    floodfill(matrix, row + 1, col)
                if col > 0:
                    floodfill(matrix, row, col - 1)
                if col < len(matrix[row]) - 1:
                    floodfill(matrix, row, col + 1)
            if matrix[row][col] != 0 or matrix[row][col] != '*':
                if [row,col] not in self.showIndexs:
                    self.showIndexs += [[row,col]]
        if self.stat == GameStatus.PLAYING:
            floodfill(self.miner, row, col)
        if (self.row * self.col) - self.countMins == len(self.showIndexs):
            self.stat = GameStatus.WIN

    def status(self):
        print(self.stat.name)

    def printField(self):
        for i in range(self.row):
            print('"', end="")
            for j in range(self.col):
                if (self.stat == GameStatus.WIN or self.stat == GameStatus.LOST) and self.miner[i][j] == '*':
                    print('*', end="")
                elif [i,j] in self.showIndexs:
                    if self.miner[i][j] == 0 or self.miner[i][j] == '+':
                        print('+', end="")
                    else:
                        print(self.miner[i][j], end="")
                else:
                    print('.', end="")
            print('"')
        print()

