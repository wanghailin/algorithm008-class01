class Solution(object):
    def solveNQueens(self, n):
        col = set()
        master = set()
        slave = set()
        res , stack = [], []

        nums = [i for i in range(n)]
        self.traceBackNew(nums, n, 0, col, master, slave, stack, res)
        return res


    def traceBackNew(self, nums, n, rowNum, col, master, slave, stack, res):
        if rowNum == n:
            board = self.__convert2board(stack, n)
            res.append(board)
            return
        for i in range(n):
            if i not in col and rowNum + i not in master and rowNum - i not in slave:
                stack.append(nums[i])
                master.add(rowNum + i)
                slave.add(rowNum - i)
                col.add(i)

                self.traceBackNew(nums, n, rowNum + 1, col, master, slave, stack, res)

                master.remove(rowNum + i)
                slave.remove(rowNum - i)
                col.remove(i)
                stack.pop()

    def __convert2board(self, stack, n):
        return ["." * stack[i] + "Q" + "." * (n - stack[i] - 1) for i in range(n)]