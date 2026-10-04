class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        longest = 0
        for num in s:
            if num-1 not in s:
                new_num = num+1
                length =1
                while new_num in s:
                    length+=1
                    new_num+=1
                longest = max(longest,length)
        return longest
