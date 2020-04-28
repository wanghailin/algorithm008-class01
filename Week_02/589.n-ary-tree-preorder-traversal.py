class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        if root is None:
            return []
        res = [root.val]
        for i in root.children:
            res.extend(self.preorder(i))
        return res
"""
class Solution:
    def preorder(self, root):
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            root = stack.pop()
            result.append(root.val)
            if root.children:
                for idx in range(len(root.children) - 1, -1, -1):
                    stack.append(root.children[idx])
        return result
"""