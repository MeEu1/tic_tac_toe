from cmath import nan


class Prop:
    def __init__(self):
        self.board = [False, False, False, False, False, False, False, False, False]
        self.game = [[None, None, None], [None, None, None], [None, None, None]]
    
    def assignValue(self, value, row_column):
        if self.board[row_column[0]][row_column[1]] in self.board:
            self.board[row_column[0]][row_column[1]] = value

    def is_aligned(self):
        for i in range(len(self.game)):
            for j in range(len(self.game[i])):
                if self.game[i][j] != None:
                    if len(set(self.game[i])) == 1: #horizontal alignment
                        return True
                    elif self.game[0][j] == self.game[1][j] == self.game[2][j]: #vertical alignment
                        return True
        
        #diagonals
        if self.game[0][0] == self.game[1][1] == self.game[2][2] and self.game[0][0] != None: #left to right
            return True
        elif self.game[0][2] == self.game[1][1] == self.game[2][0] and self.game[0][2] != None: #right to left
            return True

        return False
    
    def restart(self):
        self.board = [False, False, False, False, False, False, False, False, False]
        self.game = [[None, None, None], [None, None, None], [None, None, None]]