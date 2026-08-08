class Solution:
    def rec(self,i,arr,k,dp):
        n = len(arr)

        if i == n:
            return 0
        if dp[i]  != -1:
            return dp[i]
        ans = 0
        maxi = 0
        
        for end in range(i , min(n , i+k)):
            maxi = max(maxi , arr[end])
            length = end-i +1
            current = length * maxi
            ans = max(ans, current+ self.rec(end+1,arr,k,dp))
        dp[i] = ans
        return dp[i]


    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [-1]*n
        return self.rec(0,arr,k,dp)       