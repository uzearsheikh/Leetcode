import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = []
        for i in range(n):
            adjlist.append([])
        for edge in times:
            x= edge[0]-1
            y = edge[1]-1
            z=edge[2]

            adjlist[x].append([y,z])
            
        visited = [False]*(n)
        heap = []      
        distance_from_source = [float('inf')]*(n)
        k-=1
        distance_from_source[k] = 0
        visited[k]= True
        heappush(heap,(distance_from_source[k],k))

        while len(heap)>0:
            d,u = heapq.heappop(heap)    # d= distance u = node which is currently just visited

            for v,z in adjlist[u]:
                if distance_from_source[u] + z< distance_from_source[v]:
                    distance_from_source[v] = distance_from_source[u] + z
                    heappush(heap , (distance_from_source[v],v))
        ans = max(distance_from_source)
        if ans == float('inf'):
            return -1
        else:
            return ans

        
        