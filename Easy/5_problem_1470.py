#https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = 0
        y = n
        final_nums = []
        for i in range(n):
            final_nums.append(nums[x])
            final_nums.append(nums[y])
            x += 1
            y += 1
        return final_nums
    
        """
        or
        for i in range(n):
            nums.insert(2*i+1, nums[n+2*i])
        return nums[:2*n]
        """