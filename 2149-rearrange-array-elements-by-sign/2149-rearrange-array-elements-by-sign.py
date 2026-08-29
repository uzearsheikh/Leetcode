class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive , negative =[],[]
        for i in nums:
            if i > 0:
                positive.append(i)
            else:
                negative.append(i)
        ans = []
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans