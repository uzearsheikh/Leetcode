class Solution:

    def rec(self, i, s, dp):

        if i == len(s):
            return 0

        if dp[i] != -1:
            return dp[i]

        ans = float("inf")

        for end in range(i, len(s)):

            if s[i:end+1] == s[i:end+1][::-1]:

                ans = min(ans, 1 + self.rec(end + 1, s, dp))

        dp[i] = ans
        return dp[i]

    def minCut(self, s: str) -> int:

        n = len(s)
        dp = [-1] * n

        return self.rec(0, s, dp) - 1