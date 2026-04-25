class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res,sol =[],[]
        # i is index
        def backtrack(i):
            if i == n: # we reach to last element of the given list this i sour base case
                res.append(sol.copy())
                return 
            
            #dont pick nums[i]
            backtrack(i+1)

            # pic nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res

        