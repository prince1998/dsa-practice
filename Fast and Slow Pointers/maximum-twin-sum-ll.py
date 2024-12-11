# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

def twin_sum(head):
  low = head
  high = head
  
  while high and high.next:
    low = low.next
    high = high.next.next
    
  prev = None
  next = None
  curr = low
  while curr != None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    
  max_sum = 0
  start = head
  while prev != None:
    sum = start.data + prev.data
    if sum > max_sum:
      max_sum = sum
    start = start.next
    prev = prev.next

    
  return max_sum

