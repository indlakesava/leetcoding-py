#https://leetcode.com/problems/two-sum/
#1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums.copy()
        nums.sort()
        i = 0
        j = len(nums)-1
        lst = []
        
        while(i<j):
            if(nums[i]+nums[j]>target):
                j = j-1
            elif(nums[i]+nums[j]<target):
                i = i+1
            else:
                for k in range(len(temp)):
                    if(nums[i] == temp[k]):
                        lst.append(k)
                    elif(nums[j] == temp[k]):
                        lst.append(k)
                return lst
