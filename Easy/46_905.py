https://leetcode.com/problems/sort-array-by-parity/
#905
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_lst = []
        odd_lst = []
        for i in nums:
            if(i%2==0):
                even_lst.append(i)
            else:
                odd_lst.append(i)
                
        return even_lst+odd_lst
