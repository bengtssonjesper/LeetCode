# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        s2 = ""
        res = []
        curr = l1

        while(curr != None):
            s1 += str(curr.val)
            curr = curr.next

        curr = l2
        while(curr != None):
            s2 += str(curr.val)
            curr = curr.next

        s1 = s1[::-1]  # Reverse order
        s2 = s2[::-1]
        intsum = int(s1)+int(s2)
        strsum = str(intsum)
        strsum = strsum[::-1]

        head = ListNode(int(strsum[0]))

        curr = head

        for i in range(1, len(strsum)):
            curr.next = ListNode(int(strsum[i]))
            curr = curr.next
        return head
