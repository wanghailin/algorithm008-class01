class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        gi = si = res = 0
        while gi < len(g) and si < len(s):
            if g[gi] <= s[si]:
                gi += 1
                si += 1
                res += 1
            else:
                si += 1
        return res