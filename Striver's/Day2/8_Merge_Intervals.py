#https://leetcode.com/problems/merge-intervals/
'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''

class Solution:
    def merge(intervals):
        intervals.sort(key=lambda pair : pair[0])
        output = [intervals[0]]

        for start, end in intervals:
            prevend = output[-1][1]

            if start<=prevend:
                output[-1][1] = max(prevend, end)
            else:
                output.append([start, end])
        return output

print(Solution.merge([[1,3],[2,6],[8,10],[15,18]]))
'''
Explanation:
Sort the given array based on the start time using lambda function
Now we have a new output variable and start iterating over sorted intervals array
at each step we check if the current start point is less than or equal to previous endpoint 
if yes then we modify the end time of last interval in output array to the maximum of that end time and current end time
'''