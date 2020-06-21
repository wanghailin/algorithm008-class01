# coding=utf-8
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
#  Note: You may assume the string contain only lowercase English letters.
#  Related Topics 哈希表 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for char in s:
            dic[char] = dic.setdefault(char, 0) + 1
        for char in s:
            if dic.get(char) == 1:
                return char

# leetcode submit region end(Prohibit modification and deletion)
