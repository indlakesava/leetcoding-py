#https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
'''
Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
Note: Unlike 0/1 knapsack, you are allowed to break the item here.

Example 1:
Input:
N = 3, W = 50
value[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.000000
Explanation:
Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, to fit it into weight 20. so it becomes (120/30)*20=80, so the total weight becomes 60+100+80.0=240.0
Thus, total maximum value of item we can have is 240.00 from the given capacity of sack.

Example 2:
Input:
N = 2, W = 50
value[] = {60,100}
weight[] = {10,20}
Output:
160.000000
Explanation:
Take both the items completely, without breaking.
Total maximum value of item we can have is 160.00 from the given capacity of sack.
Your Task :
Complete the function fractionalKnapsack() that receives maximum capacity , array of structure/class and size N and returns a double value representing the maximum value in knapsack.
Note: The details of structure/class is defined in the comments above the given function.

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= W <= 109
1 <= valuei, weighti <= 104
'''

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w

class Solution:
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(W,arr,n):
        # code here
        arr.sort(key = lambda x : x.value/x.weight, reverse=True)
        result = 0
        curWeight = 0
        for i in range(n):
            if curWeight+arr[i].weight<=W:
                curWeight += arr[i].weight
                result += arr[i].value
            else:
                remain = W - curWeight
                result += (arr[i].value / arr[i].weight) * remain
                break
        return result

'''
The greedy method to maximize our answer will be to pick up the items with higher values. 
Since it is possible to break the items as well we should focus on picking up items having 
higher value /weight first. To achieve this, items should be sorted in decreasing order 
with respect to their value /weight. Once the items are sorted we can iterate. 
Pick up items with weight lesser than or equal to the current capacity of the knapsack. 
In the end, if the weight of an item becomes more than what we can carry, 
break the item into smaller units. Calculate its value according to our current capacity 
and add this new value to our answer.
'''