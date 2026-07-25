class Solution:

    def cost(self, s, left, right):

        changes = 0

        while left < right:

            if s[left] != s[right]:
                changes += 1

            left += 1
            right -= 1

        return changes

    def rec(self, i, k, s, dp):

        n = len(s)

        # Success
        if i == n and k == 0:
            return 0

        # Invalid
        if i == n:
            return float('inf')

        if k == 0:
            return float('inf')

        # Optional Pruning
        if n - i < k:
            return float('inf')

        if dp[i][k] != -1:
            return dp[i][k]

        ans = float('inf')

        for end in range(i, n):

            current = self.cost(s, i, end)

            ans = min(
                ans,
                current + self.rec(end + 1, k - 1, s, dp)
            )

        dp[i][k] = ans
        return dp[i][k]

    def palindromePartition(self, s: str, k: int) -> int:

        n = len(s)

        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        return self.rec(0, k, s, dp)