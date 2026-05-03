class Solution:
    def partition(self, s):
        res = []
        sol = []
        
        def isPalindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start):
            # base condition
            if start == len(s):
                res.append(sol[:])
                return
            
            for end in range(start, len(s)):
                if isPalindrome(s[start:end+1]):
                    
                    # TAKE
                    sol.append(s[start:end+1])
                    
                    backtrack(end + 1)
                    
                    # NOT TAKE (backtrack)
                    sol.pop()
        
        backtrack(0)
        return res