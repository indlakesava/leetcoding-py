class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        for i in range(len(candies)):
            if((candies[i]+extraCandies) >= max_candies):
                candies[i] = True
            else:
                candies[i] = False
        return candies
        """
        or using list comprehension
        max_candies = max(candies)
        candies = [True if (i+extraCandies)>=max_candies else False for i in candies]
        return candies
        """