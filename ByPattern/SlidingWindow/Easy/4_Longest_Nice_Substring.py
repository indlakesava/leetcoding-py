#https://leetcode.com/problems/longest-nice-substring/description/
'''
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

Example 1:
Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:
Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

Example 3:
Input: s = "c"
Output: ""
Explanation: There are no nice substrings.


Constraints:
1 <= s.length <= 100
s consists of uppercase and lowercase English letters.
'''

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for ii in range(i+1, len(s)+1):
                if all(s[k].swapcase() in s[i:ii] for k in range(i, ii)):
                    ans = max(ans, s[i:ii], key=len)
        return ans

    def longestNiceSubstring1(self, s: str) -> str:
        if not s: return "" # boundary condition
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss:
                s0 = self.longestNiceSubstring(s[:i])
                s1 = self.longestNiceSubstring(s[i+1:])
                return max(s0, s1, key=len)
        return s

'''
Apparently, the small size doesn't give me enough motivation to seek more efficient algo. 
Above is the implementation of divide and conquer in Python3 of this post. 
This is indeed a lot faster than the naive solution above. Credit goes to original author.
'''
