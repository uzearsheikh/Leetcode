class Solution:
    def rec(self,i,j,word1,word2,dp):
        
        if i == len(word1):
            return len(word2)-j
        if j == len(word2):
            return len(word1)-i
        if dp[i][j]!=-1:
            return dp[i][j]
        if word1[i]==word2[j]:
            dp[i][j] = self.rec(i+1, j+1, word1, word2, dp)
            return dp[i][j]
        
        # delete
        delete = 1+ self.rec(i+1,j,word1,word2,dp)
        # insert
        insert =   1+ self.rec(i,j+1,word1,word2,dp)
        # replace
        replace = 1+ self.rec(i+1,j+1,word1,word2,dp)

        dp[i][j] = min(delete,insert,replace)
        return dp[i][j]
    def minDistance(self, word1: str, word2: str) -> int:
        m , n = len(word2) , len(word1)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        return self.rec(0,0,word1,word2,dp)
        