#https://leetcode.com/problems/linked-list-cycle-ii/description/
'''
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed).
It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(head):
        slow = head
        fast = head
        temp = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                while(slow!=temp):
                    slow = slow.next
                    temp = temp.next
                return slow
        return None

'''
Explanation:
Brute force approach would be to store each node in a hashmap or set to find if we come across a repeated value and return
In this solution we use fast and slow pointers and once both of them meet at a point then we start traversing one node at a time
from both meetup point and start point until we find the collision point and that would be the start of the Linked list cycle
Maths:
L1= start to start of cycle
L2 = start of cycle to the collision point
c = cycle length

s travels L1+L2
f travels L1+L2+nc
2s = f
2L1+2L2 = L1+L2+nc
L1 = nc-L2
'''