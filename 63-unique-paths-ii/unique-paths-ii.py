class Solution:
    def rec(self,i,j,obstacleGrid,dp):
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Out of Grid
        if i >= m or j >= n:
            return 0

        # Obstacle
        if obstacleGrid[i][j] == 1:
            return 0

        # Destination
        if i == m - 1 and j == n - 1:
            return 1
        if dp[i][j]!=-1:
            return dp[i][j]
        down = self.rec(i+1,j,obstacleGrid,dp)
        right = self.rec(i,j+1,obstacleGrid,dp)
        dp[i][j]= down+right
        return dp[i][j]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1] * n for _ in range(m)]
        return self.rec(0,0,obstacleGrid,dp)
        