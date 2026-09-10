from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        output = [[-1]*cols for _ in range(rows)]
        frontier = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    output[i][j] = 0
                    frontier.append((i, j))

        while frontier:
            ci, cj = frontier.popleft()
            for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni, nj = ci+di, cj+dj
                if 0 <= ni < rows and 0 <= nj < cols and output[ni][nj] == -1:
                    output[ni][nj] = output[ci][cj] + 1
                    frontier.append((ni, nj))

        return output