class Solution:
    def subarraySum(self, nums, k):
        hashmap = {0:1}
        count = 0 
        prefix_sum = 0

        for i in nums:
            prefix_sum +=i
            required = prefix_sum - k
            if required in hashmap:
                count+=hashmap[required]
            hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
        return count
            
