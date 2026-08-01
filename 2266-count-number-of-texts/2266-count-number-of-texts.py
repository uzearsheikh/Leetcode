class Solution:

    def countTexts(self, pressedKeys: str) -> int:

        MOD = 10**9 + 7
        n = len(pressedKeys)

        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):

            limit = 4 if pressedKeys[i] == '7' or pressedKeys[i] == '9' else 3

            for j in range(i, min(i + limit, n)):

                if pressedKeys[j] != pressedKeys[i]:
                    break

                dp[i] = (dp[i] + dp[j + 1]) % MOD

        return dp[0]