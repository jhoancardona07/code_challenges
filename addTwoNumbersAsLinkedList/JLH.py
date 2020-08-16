class ListNode(object):
  def __init__(self, x=None, head=None):
    self.val = x
    self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        head=ListNode()
        result=ListNode(0)
        head.next=result
        while(l1!=None and l2!=None):
            result.next=ListNode()
            result=result.next
            result.val=l1.val+l2.val+c
            if(result.val>=10):
                result.val=result.val-10
                c=1
            else:
                c=0
            l1=l1.next
            l2=l2.next
        if (c==1):
            result.next=ListNode(1)
        return head.next.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

while result:
  print (result.val,)
  result = result.next
