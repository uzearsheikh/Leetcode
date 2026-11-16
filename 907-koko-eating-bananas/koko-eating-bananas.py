class Solution:
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)
        ans = right

        while left <= right:

            mid = (left + right) // 2
            total_hours = 0

            for pile in piles:
                hours = (pile + mid - 1) // mid
                total_hours += hours

            if total_hours <= h:
                ans = mid
                right = mid - 1

            else:
                left = mid + 1

        return ans