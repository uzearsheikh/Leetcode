class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        i = 0
        boxTypes.sort(key = lambda x : -x[1])
        n = len(boxTypes)
        while i<n and truckSize>0:
            max_box = min(truckSize , boxTypes[i][0])
            ans+= max_box * boxTypes[i][1]
            truckSize-=max_box
            i+=1
        return ans
        