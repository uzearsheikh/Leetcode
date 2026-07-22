class Solution:
    def maxProduct(self, s: str) -> int:
        pal = []

        def dfs(i, cur, used):

            if i == len(s):
                if cur == cur[::-1]:
                    pal.append((cur, used.copy()))
                return

            # skip
            dfs(i + 1, cur, used)

            # take
            used.add(i)
            dfs(i + 1, cur + s[i], used)
            used.remove(i)

        dfs(0, "", set())

        ans = 0
        for i in range(len(pal)):
            for j in range(i + 1, len(pal)):

                s1, idx1 = pal[i]
                s2, idx2 = pal[j]

                if idx1.isdisjoint(idx2):
                    ans = max(ans, len(s1) * len(s2))

        return ans