#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p = 1
        s = 0
        for i in str(n):
            s += int(i)
            p *= int(i)
        return p-s