class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mp = {}
        for i in range(n):
            need = target - nums[i]
            if need in mp:
                return [mp[need],i]
            else:
                mp[nums[i]] = i
        
            
            