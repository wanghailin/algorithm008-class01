#coding=utf-8
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res
'''
基本思想就是
A 先从左子树开始，把所有左子树塞入stack
B 没有左子树之后，
    step1 . pop出stack栈，将当前节点值加入返回数组
    step2 . 找对应的右子树,将右子树塞入stack
重复直到stack为空
'''