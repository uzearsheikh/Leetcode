class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        jump_val = 0
        
        for i in range(len(nums)):
            
            if i > jump_val:
                return False
            
            jump_val = max(jump_val, i + nums[i])
        
        return True