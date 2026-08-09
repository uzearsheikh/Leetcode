class Solution:
    def ispalindrome(self, start, end, s):
        return s[start:end+1] == s[start:end+1][::-1]

    def rec(self, i, s):
        if i == len(s):
            return 0

        ans = 0

        for end in range(i, len(s)):
            if self.ispalindrome(i, end, s):
                ans += 1

        final_ans = ans + self.rec(i + 1, s)
        return final_ans
    def countSubstrings(self, s: str) -> int:
        return self.rec(0, s)