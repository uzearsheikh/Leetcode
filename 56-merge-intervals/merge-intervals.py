class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()   # har baar sorted testcase nhi aate 

        i = 0
        while i < len(intervals) - 1:
            
            if intervals[i][1] < intervals[i+1][0]:
                i += 1
                continue
            
            # overlap case
            intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
            intervals.pop(i+1)   # next interval remove
            # i ko increment nahi karenge, kyunki new interval phir se check hoga

        return intervals
