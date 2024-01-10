#https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(list1, list2):
        result = ListNode(0, None)
        dummy = result
        while list1 and list2:
            if list1.val<list2.val:
                result.next = ListNode(list1.val, None)
                result = result.next
                list1 = list1.next
            else:
                result.next = ListNode(list2.val, None)
                result = result.next
                list2 = list2.next

        if list1:
            result.next = list1
        if list2:
            result.next = list2

        return dummy.next

'''
Explanation:
We create a new linked list by having 2 pointers, 1 in each array and picking the least among both 
Once we reach end of either of the array we then take the remaining part of the arry whose end is not yet reached
'''