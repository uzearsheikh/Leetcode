class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        a = []

        for ch in s:
            if ch != "#":
                a.append(ch)
            elif a:
                a.pop()

        b = []

        for ch in t:
            if ch != "#":
                b.append(ch)
            elif b:
                b.pop()

        return a == b