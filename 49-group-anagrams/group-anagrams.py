class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in freq:
                freq[key]=[]
            freq[key].append(i)
        ans = []

        for i in freq.values():
            ans.append(i)

        return ans

        