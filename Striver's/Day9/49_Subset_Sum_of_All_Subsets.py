#https://www.geeksforgeeks.org/problems/subset-sums2234/1
'''
Given a list arr of N integers, return sums of all subsets in it.

Example 1:
Input:
N = 2
arr[] = {2, 3}
Output:
0 2 3 5
Explanation:
When no elements is taken then Sum = 0.
When only 2 is taken then Sum = 2.
When only 3 is taken then Sum = 3.
When element 2 and 3 are taken then
Sum = 2+3 = 5.

Example 2:
Input:
N = 3
arr = {5, 2, 1}
Output:
0 1 2 3 5 6 7 8
Your Task:
You don't need to read input or print anything. Your task is to complete the function subsetSums() which takes a list/vector and an integer N as an input parameter and return the list/vector of all the subset sums.

Expected Time Complexity: O(2N)
Expected Auxiliary Space: O(2N)

Constraints:
1 <= N <= 15
0 <= arr[i] <= 104
'''

class Solution:
	def subsetSums(arr, N):
		# code here
		ans = []

		def subsetSumHelper(index, sum):
		    if index==N:
		        ans.append(sum)
                return
            subsetSumHelper(index+1, sum+arr[index])
            subsetSumHelper(index+1, sum)

        subsetSumHelper(0, 0)
        ans.sort()
        return ans

'''
Explanation:
Intuition: The main idea is that on every index you have two options either to select the element to add it to your subset(pick) or not select the element at that index and move to the next index(non-pick).
Approach: Traverse through the array and for each index solve for two arrays, one where you pick the element,i.e add the element to the sum or don’t pick and move to the next element, recursively, until the base condition. Here when you reach the end of the array is the base condition.
'''