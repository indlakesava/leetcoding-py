#https://www.interviewbit.com/problems/repeat-and-missing-number-array/
'''
You are given a read only array of n integers from 1 to n.
Each integer appears exactly once except A which appears twice and B which is missing.
Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Note that in your output A should precede B.

Example:
Input:[3 1 2 5 3]
Output:[3, 4]

A = 3, B = 4
'''

class Solution:
    def repeatedNumber(A):
        xr = 0
        for i in range(len(A)):
            xr = xr ^ A[i]
            xr = xr ^ (i+1)

        bit_no = 0
        while(1):
            if((xr & (1<<bit_no))!=0):
                break
            bit_no += 1

        zeros = 0
        ones = 0
        for i in range(len(A)):
            if((A[i] & (1<<bit_no))!=0):
                ones = ones ^ A[i]
            else:
                zeros = zeros ^ A[i]

        for i in range(1, len(A)+1):
            if((i & (1<<bit_no))!=0):
                ones = ones ^ i
            else:
                zeros = zeros ^ i

        cnt = 0
        for i in A:
            if i==zeros:
                cnt += 1

        if cnt==2:
            return [zeros, ones]
        else:
            return [ones, zeros]

    def repeatedNumber1(A):
        n = len(A)

        sn = (n*(n+1))/2
        s2n = (n*(n+1)*(2*n+1))/6
        s = 0
        s2 = 0
        for i in A:
            s += i
            s2 += i*i

        val1 = s-sn
        val2 = s2-s2n

        val2 = val2/val1

        x = (val1+val2)/2
        y = x-val1

        return [int(x), int(y)]

print(Solution.repeatedNumber([3,1,2,5,3]))
print(Solution.repeatedNumber1([3,1,2,5,3]))

'''
Explanation-1:
first we find xor of all the numbers in the array and the other array with numbers from 1 to length of array
Since xor of same numbers is 0, we will be left with the xor of missing and repeated number 
In the next step we find which of the bit is different amongst these 2 
using this bit we can create 2 groups which have 1 at that bit and zero at that bit
doing xor withing groups will left us with missing and repeated number in 2 groups
Next step is to find which one is missing and repeating, for that we pick one and iterate over the array to check count
if it gives zero then it is the missing the other will be repeated

Explanation2:
basic math
first we find the sum and sum of squares for array with numbers from 1 to length of array
then we do the same for this given array
we calculate x-y & x2-y2 = (x-y)(x+y)
we divide 2 with 1 to get x+y
once we have both the equations values, we just add and divide by 2 to get x and get y later
'''