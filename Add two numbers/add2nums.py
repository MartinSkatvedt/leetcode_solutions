class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        current_1 = l1
        current_2 = l2

        head = ListNode() 
        current_ret = head
        carry = 0

        while True:
            ans = current_1.val + current_2.val
            ans += carry

            if ans >= 10:
                carry = 1
                ans -= 10
            else:
                carry = 0
    
            temp = ListNode(ans)
            current_ret.next = temp
            current_ret = temp
            current_1 = current_1.next
            current_2 = current_2.next

            if current_1 == None and current_2 == None and carry == 0:
                break
                
            if current_1 == None:
                current_1 = ListNode()
            if current_2 == None:
                current_2 = ListNode()

        return head.next
