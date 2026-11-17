class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]]+=1
        ans=0
        max_freq = 0
        for i in freq:
            if freq[i]>max_freq:
                ans = i
                max_freq = freq[i]
        return ans
        