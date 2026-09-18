class Solution {

    public int fibo(int n, int[] dp) {

        if (n <= 1) {
            return n;
        }

        if (dp[n] != -1) {
            return dp[n];
        }

        dp[n] = fibo(n - 1, dp) + fibo(n - 2, dp);

        return dp[n];
    }

    public int fib(int n) {

        int[] dp = new int[n + 1];

        // -1 se initialize
        for (int i = 0; i <= n; i++) {
            dp[i] = -1;
        }

        return fibo(n, dp);
    }
}