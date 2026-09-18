class Solution {
    public int rec(int i , int[] cost , int[] dp){
        if(i>=cost.length) return 0;
        if (dp[i]!=-1) return dp[i];
        int one_step = rec(i+1,cost,dp);
        int two_step = rec(i+2,cost,dp);
        dp[i] = cost[i]+Math.min(one_step , two_step);
        return dp[i];
    }
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] dp = new int[n+1];
        for(int i = 0 ; i<=n;i++){
            dp[i] =-1;
            }
        int i = 0;
        return Math.min(rec(0,cost,dp),rec(1,cost,dp));
        
    }
}