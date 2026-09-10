class Solution(object):
    # 2 - alive but about to die
    # 3 - dead but live
    def liveNeighbors(self,i,j, board):
        array = [0,-1,1]
        count=0
        for m in array:
            for n in array:
                if (m!=0 or n!=0) and i+m>=0 and i + m < len(board) and n+j>=0 and n+j < len(board[i]):
                    if board[i+m][j+n] == 1 or board[i+m][j+n] == 2:
                        count+=1
        return count
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range (0, len(board)):
            for j in range (0, len(board[i])):
                if board[i][j] == 1 and (self.liveNeighbors(i,j,board)<2 or self.liveNeighbors(i,j,board)>3):
                    board[i][j] = 2
                elif board[i][j] == 0 and self.liveNeighbors(i,j,board)==3:
                    board[i][j] = 3
        for i in range (0, len(board)):
            for j in range (0, len(board[i])):
                if board[i][j] == 3:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0
        
        
    