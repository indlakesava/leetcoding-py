#https://leetcode.com/problems/number-of-recent-calls/
#933
class RecentCounter:
    def __init__(self):
        self.lst = []
        self.final_lst = []

    def ping(self, t: int) -> int:
        self.lst.append(t)
        while((self.lst[-1]-self.lst[0]) >3000):
            self.lst.pop(0)
        self.final_lst.append(len(self.lst))
            
        return self.final_lst[-1]
