class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        n = len(nums)
        res = []
        sol = []
        visited = [False] * n

        def backtrack():

            if len(sol) == n:
                res.append(sol.copy())
                return

            for i in range(n):

                if visited[i]:
                    continue

                # Duplicate skip
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue

                visited[i] = True
                sol.append(nums[i])

                backtrack()

                sol.pop()
                visited[i] = False

        backtrack()
        return res