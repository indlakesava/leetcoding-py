#https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
'''
Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".

Example 3:
Input: s = "abc"
Output: 1


Constraints:
3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {'a' : 0, 'b' : 0, 'c' : 0}
        left = 0
        right = 0
        res = 0

        while right<len(s):
            d[s[right]] += 1
            while d['a']>0 and d['b']>0 and d['c']>0:
                res += len(s)-right
                d[s[left]] -= 1
                left += 1
            right += 1
        return res

'''
Explanation:
We try to save the frequency of a,b,c in dictionary. We use left and right pointers to slide through the windows
at each point we increment the frequency of corresponding element and we check if all of them are present
if yes then we increment the result which means it is considered as a new substring, then we move the left pointer
this way we will reach the end and finally resturn the total number of substrings found
'''
