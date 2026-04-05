class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -stones[i]   #max heap bana rhe hai - use rkek max heap hoata hai  sare elemnts negative
        heapq.heapify(stones)

        while 1<len(stones):
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)

            if largest != second_largest:
                heapq.heappush(stones , largest - second_largest)
        if len(stones)==1:
            return -heapq.heappop(stones)
        else:
            return 0

            #TC = O(NLOGN) SC = O(1)