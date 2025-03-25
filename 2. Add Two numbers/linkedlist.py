from typing import Optional

def createLinkedList(l):
    if not l:
        return None
    head = ListNode(l[0])
    current = head
    for val in l[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def reverse(head):
    num = []
    current = head
    while current:
        num.append(current.val)
        current = current.next
    num.reverse()
    num = int("".join(map(str,num)))
    return num
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if isinstance(l1, list):
            l1 = createLinkedList(l1)
        if isinstance(l2,list):
            l2 = createLinkedList(l2)
        l1 = reverse(l1)
        l2 = reverse(l2)    
        l3 = str(l1+l2)
        l3 = list(map(int,l3))
        l3.reverse()
        l3 = createLinkedList(l3)
        return l3

solve = Solution()

result = solve.addTwoNumbers([2,4,3],[5,6,4])


#print(l1)
#print(l2)