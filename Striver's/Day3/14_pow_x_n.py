#https://leetcode.com/problems/powx-n/description/
'''
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:
-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
'''

class Solution:
    def myPow(x, n):
        def function(base=x, exponent=abs(n)):
            if(exponent==0):
                return 1
            elif exponent%2==0:
                return function(base*base, exponent//2)
            else:
                return base*function(base*base, (exponent-1)//2)
        f = function()

        return float(f) if n>=0 else 1/f

print(Solution.myPow(2.0000, 10))
'''
Explanation:
we try to solve this using recursion
end point of recursion is when exponent is 0 return 1
now we have 2 options, either the exponent is even or odd
if even we do x2 and x power n/2
if odd we do x*x2 and x power (n-1)/2

finally return float of final value if exponent is positive number else return 1/final value
'''