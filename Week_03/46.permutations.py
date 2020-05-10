class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, path, depth, used, res):
            if depth == len(nums):
                res.append(path[:])
            else:
                for i in range(len(nums)):
                    if not used[i]:
                        used[i] = True
                        path.append(nums[i])
                        dfs(nums, path, depth + 1, used, res)
                        used[i] = False
                        path.pop()
        res = []
        used = [False] * len(nums)
        dfs(nums, [], 0, used, res)
        return res