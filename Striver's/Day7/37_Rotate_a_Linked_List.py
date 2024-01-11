#https://leetcode.com/problems/rotate-list/description/
'''
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:
The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
'''

class Solution:
    def rotateRight(head, k):
        if not head or k==0:
            return head

        length = 1
        moving = head

        while moving.next:
            length += 1
            moving = moving.next

        moving.next = head
        k = k%length

        start = None
        length = length - k - 1
        moving = head

        for i in range(length):
            moving = moving.next

        start = moving.next
        moving.next = None

        return start

'''
Explanation:
First we find the length of the linked list and then if k>length we do k=k%length
During this step itself once we reach the end of the list we point it's next to head
Now we take a pointer as moving and then move it lenght-k-1 times from head and point it's next as start
and make the next of moving pointer as None to break the connection and mark it as end  
'''