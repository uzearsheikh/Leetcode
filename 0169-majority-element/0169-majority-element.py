class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count = 0
        # candidate = None
        # for i in range(len(nums)):
        #     if count == 0:
        #         candidate = nums[i]
        #     if nums[i] == candidate:
        #         count+=1
        #     else:
        #         count-=1
        # return candidate
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            freq[i]+=1
        
        max_freq = 0
        ans = -1

        for key in freq:

            if freq[key] > max_freq:
                max_freq = freq[key]
                ans = key

        return ans