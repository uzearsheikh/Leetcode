class Solution:
    def isPalindrome(self, start, end, s):
        return s[start:end+1] == s[start:end+1][::-1]

    def partition(self, s: str):
        res = []
        sol = []

        def rec(i):

            # Base Case
            if i == len(s):
                res.append(sol.copy())
                return

            # Try every possible partition
            for end in range(i, len(s)):

                # Valid partition?
                if self.isPalindrome(i, end, s):

                    # Choose
                    sol.append(s[i:end+1])

                    # Explore
                    rec(end + 1)

                    # Undo
                    sol.pop()

        rec(0)
        return res