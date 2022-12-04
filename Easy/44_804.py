#https://leetcode.com/problems/unique-morse-code-words/
#804
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lst = []
        morose = {'a' : ".-",'b' : "-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        
        for i in words:
            temp = ''
            for j in i:
                temp += morose[j]
            lst.append(temp)
        
        return len(set(lst))
