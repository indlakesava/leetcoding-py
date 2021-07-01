#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = [0]*(max(nums)+1)
        
        for i in nums:
            lst[i] += 1
            

        for i in range(1, len(lst)):
            lst[i] += lst[i-1]

        
        for i in range(len(nums)):
            pos = nums[i]
            if pos==0:
                nums[i]=0
            else:
                nums[i] = lst[pos-1]
            
        return nums
    
        """
        lst = []
        for i in nums:
            count = 0
            for j in nums:
                if j<i:
                    count+=1
            
            lst.append(count)
            
        return lst
        """