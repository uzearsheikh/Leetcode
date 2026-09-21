class Solution {
    public int maxProfit(int[] prices) {
        // Initialize minPrice to the first element
        int minPrice = prices[0];
        
        // Initialize maxProfit to 0 (no profit if no valid transaction possible)
        int maxProfit = 0;
        
        // Traverse through the array once - O(n) time complexity
        for (int i = 1; i < prices.length; i++) {
            // Calculate current profit if we bought at minPrice and sell today
            int currentProfit = prices[i] - minPrice;
            
            // Update maxProfit if current profit is higher
            maxProfit = Math.max(maxProfit, currentProfit);
            
            // Update minPrice if current price is lower than what we saw
            minPrice = Math.min(minPrice, prices[i]);
        }
        
        return maxProfit;
    }
}