#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
Given a string s, find the length of the longest
substring
 without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

class Solution:
    def lengthOfLongestSubstring(s):
        d = {}
        i = j = 0
        max_len = 0

        while(i<len(s) and j<len(s)):
            if(s[j] not in d):
                d[s[j]] = j
                j += 1
            else:
                if((d[s[j]]+1)>i):
                    i = d[s[j]] + 1
                d[s[j]] = j
                j += 1


            max_len = max(max_len, j-i)

        return max_len

    def lengthOfLongestSubstring1(s):
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res

print(Solution.lengthOfLongestSubstring("abcabcbb"))
print(Solution.lengthOfLongestSubstring1("abcabcbb"))

'''
Explanation:
We try lo have 2 pointer to define a substring and a dictionary to have the current substring elements and their indices
we keep moving the right pointer until we find a repeated element in the sunstring/dictionary
then we check the length and compare with max_length, and change the left pointer to that elements duplicate index from dictionary
we keep moving until the end of the array and return the max_length

in the second approach we use set instead of dictionary
at anypoint set contains the elements of substring we are checking
Here if we find a duplicate then we keep moving left pointer until there is no more right/current element in the set
'''