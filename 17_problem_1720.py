#https://leetcode.com/problems/decode-xored-array/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        lst = [first]        
        for i in range(len(encoded)):
            lst.append(encoded[i] ^ lst[i])
        
        return lst