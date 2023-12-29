#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

class Solution:
    def maxProfit(prices):
        profit = 0
        cur_least = prices[0]

        for price in prices:
            cur_least = min(cur_least, price)
            profit = max(profit, price-cur_least)

        return profit

print(Solution.maxProfit([7,1,5,3,6,4]))

'''
Explanation:
We initialize 2 variables, 1 for current least number and another for the maximum profit till now
At each stage we check if that is the least number if yes we update else proceed to next step which is
finding profit, here we check the profit by checking the difference between current price and least price
if this profit is more than previous profit, we replace else we continue with next days price
'''