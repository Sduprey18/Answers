# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
      count = 0
      counter = head
      while counter:
        count+=1 
        counter = counter.next
      #here your count will be the len of ur linked list 
      #and you want to go until you reach count - n - 1, because you want to chnage the pointer
      #of the one right before, so it dissapers
      current = head
      k = 0
      #this loops through the entirety of the linked list 
      while k<count:
        if k == count - n  - 1:
          #set the current pointer to be the next pointer thing
          temp = current.next
          current.next = temp.next
          return head
        current = current.next
        k+= 1
      return head.next
        