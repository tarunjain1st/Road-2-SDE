# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        txt1=''
        txt2=''
        while(l1 != None):
            txt1=txt1+str(l1.val)
            l1=l1.next
        while(l2 != None):
            txt2=txt2+str(l2.val)
            l2=l2.next    
            
        txt1 = txt1[::-1]
        txt2 = txt2[::-1]
        
        txt3 = str(int(txt1)+int(txt2))
        
        l3 = ListNode()
        l3.val = txt3[0]
        
    
        for i in txt3[1:]:
            temp = ListNode()
            temp.val = int(i)
            temp.next = l3
            l3 = temp
            
        return l3


def printLL(ll):
    temp = []
    while ll:
        temp.append(ll.val)
        ll = ll.next
    print (temp)

#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]

l1 = ListNode(val=2)
l1.next = ListNode(val=4)
l1.next.next = ListNode(val=3)

l2 = ListNode(val=5)
l2.next = ListNode(val=6)
l2.next.next = ListNode(val=4)


solve = Solution()
result = solve.addTwoNumbers(l1,l2)

printLL(result)