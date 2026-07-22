class Solution:

    def rec(self, i, j, matrix, dp):

        m = len(matrix)
        n = len(matrix[0])

        # Out of bounds
        if i >= m or j >= n:
            return 0

        # DP
        if dp[i][j] != -1:
            return dp[i][j]

        # Current cell is 0 -> square cannot start here
        if matrix[i][j] == "0":
            dp[i][j] = 0
            return 0

        # Explore 3 directions
        right = self.rec(i, j + 1, matrix, dp)
        down = self.rec(i + 1, j, matrix, dp)
        diagonal = self.rec(i + 1, j + 1, matrix, dp)

        # Current side length
        dp[i][j] = 1 + min(right, down, diagonal)

        return dp[i][j]


    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1] * n for _ in range(m)]

        ans = 0

        # Largest square can start from ANY cell
        for i in range(m):
            for j in range(n):
                ans = max(ans, self.rec(i, j, matrix, dp))

        # Question asks AREA, not side length
        return ans * ans