#https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
'''
There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?
Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

Example 1:

Input:
N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output:
4
Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)
Example 2:

Input:
N = 3
start[] = {10, 12, 20}
end[] = {20, 25, 30}
Output:
1
Explanation:
Only one meetings can be held
with given start and end timings.

Your Task :
You don't need to read inputs or print anything. Complete the function maxMeetings() that takes two arrays start[] and end[] along with their size N as input parameters and returns the maximum number of meetings that can be held in the meeting room.


Expected Time Complexity : O(N*LogN)
Expected Auxilliary Space : O(N)


Constraints:
1 ≤ N ≤ 105
0 ≤ start[i] < end[i] ≤ 105
'''

class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(n,start,end):
        # code here
        meet = [meeting(start[i], end[i], i+1) for i in range(n)]
        meet.sort(key=lambda x: (x.end, x.pos))
        answer = []
        limit = meet[0].end
        answer.append(meet[0].pos)
        for i in range(1, n):
            if meet[i].start > limit:
                limit=meet[i].end
                answer.append(meet[i].pos)
        return len(answer)

print(Solution.maximumMeetings(8,
[75250,50074, 43659, 8931, 11273, 27545, 50879, 77924],
[112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]))

'''
Explanation:
To proceed we need a vector of three quantities: the starting time, ending time, meeting number. Sort this data structure in ascending order of end time. 
We need a variable to store the answer. Initially, the answer is 1 because the first meeting can always be performed. Make another variable, say limit that keeps track of the ending time of the meeting that was last performed. Initially set limit as the end time of the first meeting.
Start iterating from the second meeting. At every position we have two possibilities:-
If the start time of a meeting is  strictly greater than limit we can perform the meeting. Update the answer.Our new limit is the ending time of the current meeting  since it was last performed.Also update limit.  
If the start time is less than or equal to limit  ,skip and move ahead.  
'''