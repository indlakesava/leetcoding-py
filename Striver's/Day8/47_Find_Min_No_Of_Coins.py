#https://takeuforward.org/data-structure/find-minimum-number-of-coins/

'''
Given an array coins[] of size N and a target value V, where coins[i] represents the coins of different denominations. You have an infinite supply of each of coins. The task is to find minimum number of coins required to make the given value V. If it’s not possible to make a change, print -1.

Examples:
Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required We can use one coin of 6 cents and 1 coin of 5 cents
'''

if __name__ == '__main__':
    V = 49
    ans = 0
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = 9
    for i in range(n - 1, -1, -1):
        while V >= coins[i]:
            num_coin_i = V//coins[i]
            V -= coins[i]*num_coin_i
            ans += num_coin_i
    print("The minimum number of coins is", ans)


'''
Approach: We will keep a pointer at the end of the array i. 
Now while(V >= coins[i]) we will reduce V by coins[i] and add it to the ans array.
We will also ignore the coins which are greater than V and the coins which are less than V. 
We consider them and reduce the value of V by coins[I].
'''