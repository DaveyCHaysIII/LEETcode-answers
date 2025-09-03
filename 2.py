"""
2. Add two numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum as a linked list.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        l3 = ListNode(0)
        current = l3
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            if total >= 10:
                current.next = ListNode(total - 10)
                carry = 1
            else :
                current.next = ListNode(total)
                carry = 0

            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return l3.next

"""
Hard Parts: didn't even really know how to approach this one,
     honestly relearning python is getting in the way of doing
     these properly. Also learned that its better to walk through
     the problem several times to really get what we need to do.
     This problem seems really easy, but getting the code to do
     what your brain wants it to do is the hard part.

Strategy: add the numbers, handle the carry

Time complexity: ON

Better solution: there are more optimal solutions but they aren't
immediately obvious and require a lot of knowlege on how python
works under the hood, which is outside of the scope of this
exercise.
"""

