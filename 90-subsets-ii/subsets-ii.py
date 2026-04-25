class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()   # 🔴 important for duplicates
        res = []
        sol = []
        n = len(nums)

        def back(i):
            # base case
            if i == n:
                res.append(sol.copy())
                return

            # ✅ PICK
            sol.append(nums[i])
            back(i + 1)
            sol.pop()

           
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            
            back(i + 1)

        back(0)
        return res