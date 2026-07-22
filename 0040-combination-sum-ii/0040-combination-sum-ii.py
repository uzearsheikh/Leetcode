class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()

        def backtrack(i,sol , total):
            if total == target:
                result.append(sol.copy())
                return
            if i == len(candidates) or total>target:
                return
           
            # include or take
            sol.append(candidates[i])
            backtrack(i+1,sol,total + candidates[i])
            sol.pop()
             # avoid duplicate
            while i+1<len(candidates) and candidates[i]== candidates[i+1]:
                i+=1
            # dont take
            backtrack(i+1,sol,total)
        backtrack(0, [],0 )
        return result


