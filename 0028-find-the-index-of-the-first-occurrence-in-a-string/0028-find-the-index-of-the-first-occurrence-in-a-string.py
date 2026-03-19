class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        
        for i in range(len(haystack)):
            curr = haystack[i:i+m]
            if curr == needle:
                return i
        return -1
            

        