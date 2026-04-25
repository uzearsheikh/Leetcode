class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol = [],[]
        n = len(candidates)
        def backtrack(i, total):
            #  base cases
            if total == target:
                res.append(sol.copy())
                return
            if i >= len(candidates) or total > target:
                return
             #  take (same index, reuse allowed)
            sol.append(candidates[i])
            backtrack(i, total + candidates[i])
            sol.pop()
            
            # skip
            backtrack(i + 1, total)
        backtrack(0,0)
        return res
            
        