class Solution:

    def rec(self, i, j, text1, text2, dp):

        if i == len(text1) or j == len(text2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:

            dp[i][j] = 1 + self.rec(i + 1, j + 1, text1, text2, dp)
            return dp[i][j]

        skip1 = self.rec(i + 1, j, text1, text2, dp)
        skip2 = self.rec(i, j + 1, text1, text2, dp)

        dp[i][j] = max(skip1, skip2)

        return dp[i][j]

    def longestCommonSubsequence(self, text1, text2):

        dp = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        return self.rec(0, 0, text1, text2, dp)