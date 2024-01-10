#https://leetcode.com/problems/palindrome-linked-list/description/
'''
Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.

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

class Solution:
    def isPalindrome(head):
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head
        while curr:
            if curr.val!=stack.pop():
                return False
            curr = curr.next
        return True

'''
Explanation:
We use stack to store the values in reverse order in first iteration
In the second iteration we again go to each node from the beginning and
at the same time check if the current node value and the top value of stack is same and continue till end
'''
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def isPalindrome(self, head):
        self.left = ListNode(0, head)

        def recursiveFunction(head):
            if not head:
                return True

            right = recursiveFunction(head.next)
            self.left = self.left.next
            return right and self.left.val==head.val

        return recursiveFunction(head)

'''
Explanation:
We use recursion for this solution and the recursion calls head.next till end so
each time head will be from the back, and we have left node to start from left
we compare both left and back val
'''

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
We first do slow and fast pointer iteration to find the middle
once we find the middle we try to reverse first half
Now we will use 2 pointers prev and head to go through the list and check if all the values are same
'''