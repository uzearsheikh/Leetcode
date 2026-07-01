class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        ans = 0
        n = len(colors)
        for i in range(1, n):
            if colors[i - 1] == colors[i]:
                ans += min(neededTime[i], neededTime[i - 1])

                # Bade wale time ko aage carry karo
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return ans


        