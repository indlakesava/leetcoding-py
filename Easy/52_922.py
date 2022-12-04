#https://leetcode.com/problems/sort-array-by-parity-ii/
#922
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        i =0
        
        while(i != len(nums)):
            if i%2==0:
                if nums[i]%2!=0:
                    odd.append(i)
            else:
                if nums[i]%2==0:
                    even.append(i)
            i+=1
            
        for i in range(len(odd)):
            nums[odd[i]], nums[even[i]] = nums[even[i]], nums[odd[i]]
            
        return nums
