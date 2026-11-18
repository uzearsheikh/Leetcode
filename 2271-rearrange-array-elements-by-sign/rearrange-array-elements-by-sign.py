class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive , negative =[],[]
        for i in nums:
            if i<0:
                negative.append(i)
            else:
                positive.append(i)
        ans = []
        for i in range(len(negative)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans
       