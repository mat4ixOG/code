from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Example:
   class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         if not head or not head.next:
            return head
         reversed_head = self.reverseList(head.next) 
         head.next.next = head
         head.next = None
         return reversed_head 

    if __name__ == '__main__':
       solution = reverseList('',[0,1,2,3])
       print(solution)