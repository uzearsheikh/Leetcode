class Solution:

    def rec(self, i, j, text1, text2,dp):

        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            dp[i][j]= 1 + self.rec(i + 1, j + 1, text1, text2,dp)
        if dp[i][j]!=-1:
            return dp[i][j]

        skip_text1 = self.rec(i + 1, j, text1, text2,dp)
        skip_text2 = self.rec(i, j + 1, text1, text2,dp)

        dp[i][j] = max(skip_text1, skip_text2)
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * (len(text2)+1) for _ in range(len(text1)+1)]

        return self.rec(0, 0, text1, text2,dp)