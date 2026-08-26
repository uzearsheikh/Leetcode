class Solution:

    def rec(self, i, j, s, p, dp):

        # Agar string khatam ho gayi
        if i == len(s):

            # Agar pattern bhi khatam ho gaya
            if j == len(p):
                return True

            # Agar remaining pattern "x*" type hai,
            # to * us character ko 0 times le sakta hai
            if j + 1 < len(p) and p[j + 1] == '*':
                return self.rec(i, j + 2, s, p, dp)

            # String khatam hai but pattern match nahi hua
            return False

        # Agar pattern khatam ho gaya but string baaki hai
        if j == len(p):
            return False

        # Agar ye state pehle calculate ho chuki hai
        if dp[i][j] != -1:
            return dp[i][j]

        # Check karo current characters match kar rahe hain ya nahi
        # "." kisi bhi ek character ko match karta hai
        match = (s[i] == p[j] or p[j] == '.')

        # Check karo ki current pattern character ke baad "*" hai
        if j + 1 < len(p) and p[j + 1] == '*':

            # Choice 1:
            # "*" ko 0 times use karo
            # Isliye pattern me j + 2 par chale jao
            skip = self.rec(i, j + 2, s, p, dp)

            # Choice 2:
            # "*" ko current character ke liye use karo
            take = False

            if match:
                # String me aage jao,
                # lekin pattern ka j same rakho
                # kyunki "*" aur characters match kar sakta hai
                take = self.rec(i + 1, j, s, p, dp)

            # Dono choices me se koi ek successful ho
            dp[i][j] = skip or take

        else:

            # "*" nahi hai aur current character match karta hai
            if match:
                # Dono string aur pattern me aage jao
                dp[i][j] = self.rec(i + 1, j + 1, s, p, dp)

            else:
                # Match nahi hua
                dp[i][j] = False

        # Current state ka answer return karo
        return dp[i][j]

    def isMatch(self, s: str, p: str) -> bool:

        n = len(s)
        m = len(p)

        # n+1 aur m+1 isliye:
        # i == n aur j == m wali states bhi aa sakti hain
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        # String aur pattern ke start se recursion
        return self.rec(0, 0, s, p, dp)