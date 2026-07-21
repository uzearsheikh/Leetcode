class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        res = 0
        for i in range(len(nums)):
           
            if nums[i] == 1:
                res+=1
            else:
                res = 0
            ans = max(ans,res)
        return ans

        