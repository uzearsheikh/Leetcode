class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        def dfs(i,j):
        # Boundary check
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return

            # Water hai
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"   #visited mark
            # 4 direction
            dfs(i - 1, j)  # up
            dfs(i + 1, j)  # down
            dfs(i, j - 1)  # left
            dfs(i, j + 1)  # right
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "1":

                    # Nayi island mili
                    count += 1

                    # Puri island visit karo
                    dfs(i, j)
        return count       


            