class Solution:

    def rec(self, i, s, wordSet, dp):

        if i == len(s):
            return True

        if dp[i] != -1:
            return dp[i]

        for end in range(i, len(s)):

            if s[i:end+1] in wordSet:

                if self.rec(end + 1, s, wordSet, dp):
                    dp[i] = True
                    return dp[i]

        dp[i] = False
        return dp[i]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)

        dp = [-1] * (len(s) + 1)

        return self.rec(0, s, wordSet, dp)