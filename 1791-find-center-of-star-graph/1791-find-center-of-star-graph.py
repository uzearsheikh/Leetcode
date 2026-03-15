class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge0 = edges[0]
        edge1 = edges[1]
        return edge0[0] if edge0[0] in edge1 else edge0[1]
        # edge 0 has 2 elements if anyone is redent in another pair then that is the center as th ecenter is common