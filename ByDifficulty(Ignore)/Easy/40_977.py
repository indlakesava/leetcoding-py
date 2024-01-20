#https://leetcode.com/problems/squares-of-a-sorted-array/
#977
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s = [i*i for i in nums]
        s.sort()
        return s
