class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] =1
            else:
                freq[i]+=1
        maxFreq = 0

        for i in freq.values():
            maxFreq = max(maxFreq, i)

        ans = 0

        for i in freq:
            if freq[i] == maxFreq:
                ans += freq[i]

        return ans