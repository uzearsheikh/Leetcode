class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        se = set()
        te =set()
        freq1 = Counter(s)
        freq2 = Counter(t)
        for i in range(len(s)):
            se.add(s[i])
        for j in range(len(t)):
            te.add(t[j])
        if len(se)!=len(te):
            return False
        if len(s)!=len(t):
            return False
        
        for i in se:
            if i not in te:
                return False
            else:
                if freq1 != freq2:
                    return False
        return True
        