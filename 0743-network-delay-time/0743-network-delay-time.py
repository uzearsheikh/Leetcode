import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjlist = []
        for i in range(n+1):
            adjlist.append([])
        for edge in times:
            x= edge[0]
            y = edge[1]
            z=edge[2]

            adjlist[x].append([y,z])
            
        visited = [False]*(n+1)
        heap = []      
        distance_from_source = [float('inf')]*(n+1)
        
        distance_from_source[k] = 0
        visited[k]= True
        heappush(heap,(distance_from_source[k],k))

        while len(heap)>0:
            d,u = heapq.heappop(heap)    # d= distance u = node which is currently just visited

            for v,z in adjlist[u]:
                if distance_from_source[u] + z< distance_from_source[v]:
                    distance_from_source[v] = distance_from_source[u] + z
                    heappush(heap , (distance_from_source[v],v))
        ans = max(distance_from_source[1:])
        if ans == float('inf'):
            return -1
        else:
            return ans

        
        