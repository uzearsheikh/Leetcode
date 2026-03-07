from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 1
        i = 1
        
        while i < len(nums):
            
            if nums[i] == nums[i-1]:
                count += 1
                
                if count > 2:
                    nums.pop(i)
                    continue
            else:
                count = 1
            
            i += 1
        
        return len(nums)
                    