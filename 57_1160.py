#https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
#1160
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d_chars = {}
        for i in chars:
            if i in d_chars:
                d_chars[i] += 1
            else:
                d_chars[i] = 1
                
        count = 0;
        
        for word in words:
            d_word = {}
            temp_count = 0
            for j in word:
                if j in d_word:
                    d_word[j] += 1
                else:
                    d_word[j] = 1
            
            for a,b in d_word.items():
                if a in d_chars:
                    if d_word[a]>d_chars[a]:
                        temp_count = 0
                        break;
                    else:
                        temp_count += d_word[a]
                    
                else:
                    temp_count = 0
                    break;
                    
            count += temp_count
            
        return count
