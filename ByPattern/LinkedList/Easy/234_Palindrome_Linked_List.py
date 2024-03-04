#https://leetcode.com/problems/palindrome-linked-list/description/
'''
Given the head of a singly linked list, return true if it is a
palindrome
 or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(head):
        if not head:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True

'''
Explanation:
we try to get the middle node and then try to reverse the second half of the linkedlist
Now we start moving both head and middle node and check if nodes at iteration is same if nit we return False else return true
'''
