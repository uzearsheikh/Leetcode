
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        
        for val in count.values():
            length += (val // 2) * 2   # even part add karo
            
            if length % 2 == 0 and val % 2 == 1:
                length += 1   # ek odd ko center me use karo
                
        return length