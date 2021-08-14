#https://leetcode.com/problems/substring-with-concatenation-of-all-words/
#30
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        w = {}
        for i in words:
            if i in w:
                w[i] += 1
            else:
                w[i] = 1
        
        buffer = len(words)*len(words[0])
        
        for i in range(len(s)-buffer+1):
            d = {}
            flag = 0
            for j in range(len(words)):
                temp = s[i+j*len(words[0]):i+len(words[0])+j*len(words[0])]
                if temp in w:
                    if temp in d:
                        d[temp] += 1
                    else:
                        d[temp] = 1
                else:
                    flag = 1
                    break
            if(flag==0):
                if d == w:
                    result.append(i)
        return result