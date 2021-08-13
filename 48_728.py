#https://leetcode.com/problems/self-dividing-numbers/
#728
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        final_lst = []
        for i in range(left, right+1):
            num = i
            lst = []
            while(i>0):
                lst.append(i%10)
                i = i//10
            flag = 0
            for j in lst:
                if j==0:
                    flag=1
                    break
                    
                if num%j!=0:
                    flag = 1
                    break
                
            if flag==0:
                final_lst.append(num)
                
        return final_lst
