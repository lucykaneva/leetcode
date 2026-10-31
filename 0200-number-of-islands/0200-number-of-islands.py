class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def out_of_bounds(i,j, arr):
            return i<0 or j<0 or i>len(arr)-1 or j>len(arr[0])-1
        def dfs (is_discovered,i,j, grid):
            neighbors = [[0,1],[0,-1],[1,0],[-1,0]]
            for pos in neighbors:
                if not out_of_bounds(i+pos[0],j+pos[1],grid) and grid[i+pos[0]][j+pos[1]] == "1" and not is_discovered[i+pos[0]][j+pos[1]]:
                    is_discovered[i+pos[0]][j+pos[1]] = True
                    dfs(is_discovered,i+pos[0],j+pos[1],grid)

        is_discovered =[[False] * len(grid[0]) for _ in range(len(grid))]
        islands = 0
        
        for i in range(0,len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and not is_discovered[i][j]:
                    is_discovered[i][j] = True
                    islands+=1
                    dfs(is_discovered,i,j,grid)
        
        return islands
        