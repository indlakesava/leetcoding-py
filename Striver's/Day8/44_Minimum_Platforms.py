#https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
'''
Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.

Example 1:
Input: n = 6
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
Output: 3
Explanation:
Minimum 3 platforms are required to
safely arrive and depart all trains.

Example 2:
Input: n = 3
arr[] = {0900, 1100, 1235}
dep[] = {1000, 1200, 1240}
Output: 1
Explanation: Only 1 platform is required to
safely manage the arrival and departure
of all trains.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findPlatform() which takes the array arr[] (denoting the arrival times), array dep[] (denoting the departure times) and the size of the array as inputs and returns the minimum number of platforms required at the railway station such that no train waits.
Note: Time intervals are in the 24-hour format(HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this may be > 59).

Expected Time Complexity: O(nLogn)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 50000
0000 ≤ A[i] ≤ D[i] ≤ 2359
'''

#User function Template for python3
class Solution:
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        platforms_needed = 1
        maximum_platforms = 1
        start = 1
        end = 0
        while start<n and end<n:
            if arr[start]<=dep[end]:
                platforms_needed += 1
                start += 1
            else:
                platforms_needed -= 1
                end += 1
            maximum_platforms = max(maximum_platforms, platforms_needed)
        return maximum_platforms

print(Solution.minimumPlatform(6, arr = [900, 945, 955, 1100, 1500, 1800],
    dep = [920, 1200, 1130, 1150, 1900, 2000]))

'''
At first we need to sort both arrays. When the events will be sorted, 
it will be easy to track the count of trains that have arrived but not departed yet. 
The total platforms needed at one time can be found by taking the difference of arrivals 
and departures at that time and the maximum value of all times will be the final answer. 
If(arr[i]<=dep[j]) means if arrival time is less than or equal to the departure time then- 
we need one more platform. So increment count as well as increment i. 
If(arr[i]>dep[j]) means the arrival time is more than the departure time then- 
we have one extra platform which we can reduce. So decrement count but increment j. 
Update the ans with max(ans, count) after each iteration of the while loop.
'''