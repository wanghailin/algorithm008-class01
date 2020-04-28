class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            if dic.get(i) == None:
                dic[i] = 1
            else:
                dic[i] = dic.get(i) + 1
        for i in t:
            if dic.get(i) == None:
                return False
            if dic.get(i) >= 1:
                dic[i] = dic.get(i) - 1
            if dic.get(i) == 0:
                dic.pop(i)
        return True