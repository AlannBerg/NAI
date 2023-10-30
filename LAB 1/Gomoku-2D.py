from easyAI import TwoPlayerGame
from easyAI.Player import Human_Player
from tabulate import tabulate


"""The board positions are numbered row + column. Board is 15x15:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 
10 11 12 13 14 15 16 17 18 19 110 111 112 113 114 
20 21 22 23 24 25 26 27 28 29 210 211 212 213 214 
30 31 32 33 34 35 36 37 38 39 310 311 312 313 314 
40 41 42 43 44 45 46 47 48 49 410 411 412 413 414 
50 51 52 53 54 55 56 57 58 59 510 511 512 513 514 
60 61 62 63 64 65 66 67 68 69 610 611 612 613 614 
70 71 72 73 74 75 76 77 78 79 710 711 712 713 714 
80 81 82 83 84 85 86 87 88 89 810 811 812 813 814 
90 91 92 93 94 95 96 97 98 99 910 911 912 913 914 
100 101 102 103 104 105 106 107 108 109 1010 1011 1012 1013 1014 
110 111 112 113 114 115 116 117 118 119 1110 1111 1112 1113 1114 
120 121 122 123 124 125 126 127 128 129 1210 1211 1212 1213 1214 
130 131 132 133 134 135 136 137 138 139 1310 1311 1312 1313 1314 
140 141 142 143 144 145 146 147 148 149 1410 1411 1412 1413 1414  
"""

'''
Created by: Alan Berg && Tomasz Fidurski.
In Gomoku to win a game player have to place
his 5 pointers next to each other in : 
row  x x x x x 
column  x
        x
        x
        x
        x

diagonally x
            x
             x
              x
                x
To choose a cell user have to type in terminal (x, y) for example for field 5,5
(5, 5)
'''

class Gomoku(TwoPlayerGame):

    def __init__(self, players):
        self.players = players
        self.board = [[0 for i in range(15)] for j in range(15)] #15x15 board
        self.boardToDisplay = self.createDisplayBoard()
        self.current_player = 1  # player 1 starts.

    def possible_moves(self):
        moves = [[ 0 for i in range(2)] for j in range(255)] # all possible moves row and column index 
        i = 0
        for row in range(15):
            for column in range(15):
                # if empty player can choose this cell
                if self.board[row][column] == 0:
                    moves[i] = row,column
                    i +=1
        return moves

    def make_move(self, move):
        row = int(move[0])
        column = int(move[1])
        playerMark = self.getPlayersMark(self.current_player)
        self.board[row][column] = playerMark
        self.boardToDisplay[row][column] = playerMark

   # def unmake_move(self, move):  # optional method (speeds up the AI)
    #    row = int(move[0])
     #   column = int(move[1])
      #  self.board[row][column] = 0

    def lose(self):
        # Does player has "five in row, column or diagonally ?" """
        playerMark = self.getOponentMark(self.current_player)
        if self.fiveMarksInRowPresent(self.board, playerMark) or self.fiveMarksInColumnPresent(self.board, playerMark) or self.fiveMarksInRightSlantPresent(self.board, playerMark) or self.fiveMarksInLeftSlantPresent(self.board, playerMark):
            print("Player with mark ", playerMark, " WIN !!!")
            return True
        return False 

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        tabulateBoard = tabulate(self.boardToDisplay, tablefmt='grid')
        print(tabulateBoard)

    def scoring(self):
        return -100 if self.lose() else 0
    
    # Creating board to display purpouse 
    def createDisplayBoard(self):
        displayBoard = [[0 for i in range(15)] for j in range(15)]
        for row in range(15):
            for column in range(15):
                displayBoard[row][column] = self.createGomokuPosition(row,column)
        return displayBoard 

    # column position as string
    def createGomokuPosition(self, rowIndex, columnIndex):
        return str(rowIndex) + str(columnIndex)
    
    # for User = B like Black, for AI = W like White
    def getPlayersMark(self, player):
        if player == 1:
            return 'B'
        return "W"
    
    # Oponent mark, for user it will return AI mark
    def getOponentMark(self, player):
         if player == 1:
            return 'W'
         return "B"

    # Return true when there is 5 playerMarks in a row
    def fiveMarksInRowPresent(self, board, playerMark):
        counter = 0
        for rowIndex in range(15):
            rowToCheck = board[rowIndex]
            for cellIndex in range(15):
                if counter == 5:
                    print(" 5 marks in row ! ", rowIndex)
                    return True
                if rowToCheck[cellIndex] == playerMark:
                    counter += 1
                else:
                    counter = 0
        return False

    # Return true when there is 5 playerMarks in a column
    def fiveMarksInColumnPresent(self, board, playerMark):
        counter = 0
        for columnIndex in range(15):
            for cellIndex in range(15):
                  if counter == 5:
                    print(" 5 marks in a column ! ", columnIndex)
                    return True
                  if board[cellIndex][columnIndex] == playerMark:
                      counter += 1
                  else:
                      counter = 0 
        return False

    #Return true when in slant / 5 marks in a row
    def goUpAdRightAndFoundFiveMarks(self, startCellRowIndex, startCellColumnIndex, maxColunIndex, playerMark, board):
        # going up and right -> row - 1, column + 1 
        currentCellRow = startCellRowIndex
        currentCellColumn = startCellColumnIndex
        counter = 0
        #print("Start sprawdzania w górę i w prawo od komórki ", startCellRowIndex, startCellColumnIndex)
        while currentCellColumn <= maxColunIndex and currentCellRow >= 0:
            #print("Sprawdzam komórkę ", currentCellRow, currentCellColumn)
            if board[currentCellRow][currentCellColumn] == playerMark:
                counter += 1
            else:
                counter = 0
            currentCellRow -= 1
            currentCellColumn += 1
            if counter == 5:
                return True
        return False

    #Return true when in slant \ 5 marks in a row
    def goDownAndRightAndFoundFiveMarks(self, startCellRowIndex, startCellColumnIndex, maxColunIndex, maxRowIndex, playerMark, board):
        # going down and right -> row + 1, column + 1 
        currentCellRow = startCellRowIndex 
        currentCellColumn = startCellColumnIndex
        counter = 0
        #print("Start sprawdzania w dół i prawo od komórki ", startCellRowIndex, startCellColumnIndex)
        while currentCellColumn <= maxColunIndex and currentCellRow <= maxRowIndex:
            #print("Sprawdzam komórkę ", currentCellRow, currentCellColumn)
            if board[currentCellRow][currentCellColumn] == playerMark:
                counter += 1
            else:
                counter = 0
            currentCellRow += 1
            currentCellColumn += 1
            if counter == 5:
                return True
        return False

    # Searching whole board to find slant / with 5 marks in a row. 0,0
    def fiveMarksInRightSlantPresent(self, board, playerMark):
        maxRowIndex = 14
        maxColunIndex = 14
        cellRowIndex = 0
        cellColumnIndex = 0
        allCellsWereChecked = False
        while not allCellsWereChecked:
            if cellRowIndex == maxRowIndex and cellColumnIndex == maxColunIndex:
                allCellsWereChecked = True
                continue
            if self.goUpAdRightAndFoundFiveMarks(cellRowIndex, cellColumnIndex, maxColunIndex, playerMark, board):
                return True
            if cellRowIndex == maxRowIndex:
                cellColumnIndex += 1
            else:
                cellRowIndex += 1 
        return False

    # Searching whole board to find slant \ with 5 marks in a row. 14,0
    def fiveMarksInLeftSlantPresent(self, board, playerMark):
        maxRowIndex = 14
        maxColunIndex = 14
        cellRowIndex = 14
        cellColumnIndex = 0
        allCellsWereChecked = False
        while not allCellsWereChecked:
            if cellRowIndex == 0 and cellColumnIndex == maxColunIndex:
                allCellsWereChecked = True
                continue
            if self.goDownAndRightAndFoundFiveMarks(cellRowIndex, cellColumnIndex, maxColunIndex, maxRowIndex, playerMark, board):
                return True
            if cellRowIndex == 0:
                cellColumnIndex += 1
            else:
                cellRowIndex -= 1 
        return False

if __name__ == "__main__":

    from easyAI import AI_Player, Negamax

#How many steps will AI think in advance
easy_ai = Negamax(2)
medium_ai = Negamax(4)
hard_ai = Negamax(6)

#Choose difficult level
ai_algo = easy_ai

Gomoku([Human_Player(), AI_Player(ai_algo)]).play()
