class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 +7
        dp = [[0]*(target+1) for _ in range(n+1)   ]      #i reperesent the no of dices j represetn the target
# base condtion 
        dp[0][0] = 1
        for dice in range(1,n+1):
            for current_sum in range(1, target+1):
                for face_value in range(1,k+1):
                    if current_sum >= face_value:
                        dp[dice][current_sum] = (dp[dice][current_sum] + dp[dice-1][current_sum-face_value])%mod
                        
        return dp[n][target]
        