class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans,sol = [],[]
        def backtrack(x):
            if len(sol)==k:
                ans.append(sol.copy())
                return
            
            left = x
            still_need = k - len(sol)  #len(sol) is the no of taken
            if left> still_need:
                backtrack(x-1)
            
            sol.append(x)
            backtrack(x-1)
            sol.pop()
        
        backtrack(n)
        return ans

        