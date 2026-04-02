class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        

        for i in range(n):
            sa = set()
            for j in range(i,n):
                if s[j] in sa:
                    break
                else:
                    sa.add(s[j])
                    l = max(l,j-i+1)
        return l
            
        
        