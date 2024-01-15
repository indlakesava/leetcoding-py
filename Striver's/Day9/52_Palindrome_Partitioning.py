#https://leetcode.com/problems/palindrome-partitioning/
'''
Given a string s, partition s such that every
substring
 of the partition is a
palindrome
. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
'''

class Solution:
    def partition(s):
        res = []
        ds = []

        def partitionHelper(ind):
            if ind==len(s):
                res.append(ds[:])
                return
            for i in range(ind, len(s)):
                if isPalindrome(s[ind:i+1]):
                    ds.append(s[ind:i+1])
                    partitionHelper(i + 1)
                    ds.pop()

        def isPalindrome(st):
            return st==st[::-1]

        partitionHelper(0)
        return res

print(Solution.partition("aab"))

'''
Approach: The initial idea will be to make partitions to generate substring and 
check if the substring generated out of the partition will be a palindrome. 
Partitioning means we would end up generating every substring and checking for palindrome at every step. 
Since this is a repetitive task being done again and again, at this point we should think of recursion. 
The recursion continues until the entire string is exhausted. After partitioning, 
every palindromic substring is inserted in a data structure When the base case has reached 
the list of palindromes generated during that recursion call is inserted in a vector of vectors/list of list.
'''