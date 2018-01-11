# Time:  O(n)
# Space: O(1)
#
# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
#

class ListNode:
    def __init__(self,x):
        x.val = x
        x.next = None

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        return l1 + l2

a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
result = Solution().addTwoNumbers(a, b)
sol = Solution()
print(sol.addTwoNumbers(l1,l2))