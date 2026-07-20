class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(intervals)):

            # Case 1: Current interval completely before newInterval
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])

            # Case 2: Current interval completely after newInterval
            elif intervals[i][0] > newInterval[1]:
                ans.append(newInterval)

                # Remaining intervals ko direct add kar do
                return ans + intervals[i:]
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        #agar end tk interval append nhi hue 
        ans.append(newInterval)
        return ans