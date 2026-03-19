class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        ans = 0
        while l<r:
            vol = min(height[l],height[r]) * (r-l)
            ans = max(ans,vol)

            if height[l]<=height[r]:
                l+=1
                
            else:
                r-=1
        return ans        

        
        