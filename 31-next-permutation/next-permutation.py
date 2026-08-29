class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        n = len(nums)

        # Step 1: Find pivot
        pivot = -1

        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # No pivot → already largest permutation
        if pivot == -1:
            nums.reverse()
            return

        # Step 2: Find element just greater than pivot
        index = -1

        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                index = i
                break

        nums[pivot], nums[index] = nums[index], nums[pivot]

        # Step 3: Reverse right part
        left = pivot + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1