class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(1, len(s), 2):
            if s[i] == s[i-1]:
                continue
            else:
                res += 1
        return res
        