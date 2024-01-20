#https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return int(''.join([str(ord(a)-97) for a in targetWord])) == int(''.join([str(ord(a)-97) for a in firstWord])) + int(''.join([str(ord(a)-97) for a in secondWord]))
        
        
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first_value = '';
        second_value = '';
        target_value = '';
        
        for i in firstWord:
            first_value += str(ord(i)-97)
        first_value = int(first_value)
        
        for i in secondWord:
            second_value += str(ord(i)-97)
        second_value = int(second_value)
        
        for i in targetWord:
            target_value += str(ord(i)-97)
        target_value = int(target_value)
        
        return first_value + second_value == target_value