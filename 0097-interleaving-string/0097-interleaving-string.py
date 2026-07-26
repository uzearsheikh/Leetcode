class Solution:
    def rec(self, i, j, s1, s2, s3, dp):

        if i == len(s1) and j == len(s2):
            return True

        if dp[i][j] != -1:
            return dp[i][j]

        k = i + j

        take_s1 = False
        take_s2 = False

        if i < len(s1) and s1[i] == s3[k]:
            take_s1 = self.rec(i + 1, j, s1, s2, s3, dp)

        if j < len(s2) and s2[j] == s3[k]:
            take_s2 = self.rec(i, j + 1, s1, s2, s3, dp)

        dp[i][j] = take_s1 or take_s2
        return dp[i][j]

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        return self.rec(0, 0, s1, s2, s3, dp)