class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res,sol = [],[]
        def backtrack(index,target):
            if target == 0:
                res.append(sol.copy())
                return
            if index==len(candidates):
                return
            if candidates[index]<=target:
                sol.append(candidates[index])
                backtrack(index,target-candidates[index])
                sol.pop()
            backtrack(index+1,target)
        backtrack(0,target)
        return res