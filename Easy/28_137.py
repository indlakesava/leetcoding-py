#https://leetcode.com/problems/single-number-ii/
#137
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for i in nums:
            ones = (ones ^ i) & ~twos
            twos = (twos ^ i) & ~ones
        
        return ones
    
    """
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        
        for i in nums:
            twos = twos | (ones & i)
            ones = ones ^ i
            common = ~(ones&twos)
            ones = ones & common
            twos = twos & common
        
        return ones
    """
