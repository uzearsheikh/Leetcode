class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def rec(i, j):

            if i > j:
                return 0

            if i == j:
                return 1

            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j] = 2 + rec(i + 1, j - 1)
            else:
                dp[i][j] = max(
                    rec(i + 1, j),
                    rec(i, j - 1)
                )

            return dp[i][j]

        return rec(0, n - 1)