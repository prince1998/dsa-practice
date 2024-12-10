# Given the head of a linked list, your task is to check whether the linked list is a palindrome or not. Return TRUE if the linked list is a palindrome; otherwise, return FALSE.

# Note: The input linked list prior to the checking process should be identical to the list after the checking process has been completed.

from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list

def palindrome(head):
  low = head
  high = head
  while high != None and high.next != None:
    low = low.next
    high = high.next.next
    
  prev = None
  curr = low
  while curr != None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  
  temp_ptr = head
  while temp_ptr and prev:
    if temp_ptr.data != prev.data:
      return False
    else:
      temp_ptr = temp_ptr.next
      prev = prev.next
  return True
    
    