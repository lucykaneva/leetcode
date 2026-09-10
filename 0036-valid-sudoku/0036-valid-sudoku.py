class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=set()
        for i in range(0, len(board)):
            for j in range (0, len(board[i])):
                if board[i][j] == '.':
                        continue
                if board[i][j] not in row:
                    row.add(board[i][j])
                else:
                    return False
            row=set()
        row=set()
        for j in range (0, len(board[0])):
            for i in range(0, len(board)):
                if board[i][j] == '.':
                        continue
                if board[i][j] not in row:
                    row.add(board[i][j])
                else:
                    return False
            row=set()
        square=set()
        
        i = 0
        j = 0

        for ind in range(0,9):   
            for m in range (i,i+3):
                for n in range(j, j+3):
                    if board[m][n] == '.':
                        continue
                    if board[m][n] not in square:
                        square.add(board[m][n])
                    else:
                        return False
            square=set()
            if i==6:
                i=0
                j+=3
            else:
                i+=3
        return True

            