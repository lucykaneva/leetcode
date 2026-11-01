class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def outOfBounds(i,j,arr):
            return i >=len(arr) or i<0 or j >=len(arr[0]) or j<0
        def dfs(grid,i,j,seen):
            neighbors = [[0,-1],[0,1],[1,0],[-1,0]]
            for pos in neighbors:
                print(pos)
                if not outOfBounds(i+pos[0],j+pos[1], grid) and grid[i+pos[0]][j+pos[1]]=="1" and not seen[i+pos[0]][j+pos[1]]:
                    seen[i+pos[0]][j+pos[1]] = True
                    print("a")

                    dfs(grid, i+pos[0],j+pos[1],seen)

        seen = [[False]*len(grid[0]) for _ in range(len(grid)) ]
        numIslands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not seen[i][j]:
                    numIslands+=1
                    seen[i][j] = True
                    dfs(grid,i,j,seen)
        return numIslands


        