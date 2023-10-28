# 200. Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water)
# , return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally
#  or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        col = len(grid[0])
        islands = 0
        visited = set()

        def dfs(grid, i, j, visited):
            if i < 0 or i >= rows or j < 0 or j >= col or grid[i][j] == '0' or (i,j) in visited:
                return
            visited.add((i,j))
            dfs(grid, i+1, j, visited)
            dfs(grid, i-1, j, visited)
            dfs(grid, i, j+1, visited)
            dfs(grid, i, j-1, visited)



        for i in range(rows):
            for j in range(col):
                if grid[i][j] == '1' and (i,j) not in visited:
                    dfs(grid, i, j, visited)
                    islands += 1
        
        return islands