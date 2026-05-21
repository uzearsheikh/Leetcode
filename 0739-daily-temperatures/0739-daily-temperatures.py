class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        n = len(temp)
        stack = []
        ans= [0]*n

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index

            stack.append(i)

        return ans

        