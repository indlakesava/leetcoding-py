#https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        j = start
        for i in range(1, n):
            j ^= start + 2*i
        return j