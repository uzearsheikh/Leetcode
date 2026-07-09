from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        n = len(nums)
        for i in nums:
            if i not in hashmap:
                hashmap[i] =1
            else:
                hashmap[i]+=1
        ans = []
        freq = Counter(hashmap)
        for i in freq:
            if freq[i]> n//3:
                ans.append(i)
        return ans
