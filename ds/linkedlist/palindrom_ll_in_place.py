"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

O(n), O(1) space
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def reverse(self, head):
        cur = head
        prev = next = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None: return True
        slow = fast = head
        prev = None
        while fast and fast.next:
            prevm slow, fast = slow, slow.next, fast.next.next

        second_half = self.reverse(slow)
        prev.next = second_half
        tmp1, tmp2 = head, second_half
        while tmp1 != second_half:
            if tmp1.val != tmp2.val:
                return False
            tmp1 = tmp1.next
            tmp2 = tmp2.next
        return True
