class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return res.values()

'''
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
a = Solution()
b = a.groupAnagrams(strs)
print(b)
'''