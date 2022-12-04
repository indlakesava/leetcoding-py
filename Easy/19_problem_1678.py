#https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        lst = []
        i = 0
        
        while i < len(command):
            if command[i] == 'G':
                lst.append('G')
                i += 1
            elif command[i:i+2] == '()':
                lst.append('o')
                i += 2
            else:
                lst.append('al')
                i += 4
        return ''.join(lst)