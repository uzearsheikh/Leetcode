class Solution:
    def rec(self, i, j, grid,dp):

        m = len(grid)
        n = len(grid[0])

        # Destination
        if i == m - 1 and j == n - 1:
            return grid[i][j]

        # Out of boundary
        if i >= m or j >= n:
            return float('inf')
        if dp[i][j] != -1:
            return dp[i][j]

        down = self.rec(i + 1, j, grid,dp)
        right = self.rec(i, j + 1, grid,dp)

        dp[i][j] =  grid[i][j] + min(down, right)
        return dp[i][j]
    def minPathSum(self, grid: List[List[int]]) -> int:

        # TOP TO BOTTOM METHOD

        # n = len(grid)
        # m = len(grid[0])

        # for i in range(1, n):
        #     grid[i][0] += grid[i-1][0]

        # for j in range(1, m):
        #     grid[0][j] += grid[0][j-1]

        # for i in range(1, n):
        #     for j in range(1, m):
        #         top = grid[i-1][j]
        #         left = grid[i][j-1]

        #         grid[i][j] += min(top, left)

        # return grid[n-1][m-1]

        # BOTTOM TO TOP
        m,n = len(grid) , len(grid[0]) 
        dp = [[-1]*n for _ in range(m)]
        return self.rec(0,0,grid,dp)