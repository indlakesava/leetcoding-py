#https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        #return '[.]'.join(address.split('.'))
        #or
        return address.replace('.','[.]') 