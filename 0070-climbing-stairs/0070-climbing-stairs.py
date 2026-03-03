# class Solution:
    # def climbStairs(self, n: int) -> int:   
    # bootm up APPROACH
#         if n==1 or n==2:
#             return n
#         first=1
#         second=2

#         for i in range(3,n+1):
#             current = first+second
#             first = second
#             second = current
#         return second

# top down approach
class Solution:
    def climbStairs(self, n: int,memo = {}) -> int:
        if n in memo:
            return memo[n]
        if n ==1:
            return 1
        if n==2:
            return 2
        
        memo[n] = self.climbStairs(n-1,memo) + self.climbStairs(n-2,memo)
        return memo[n]