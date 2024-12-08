def find_duplicate(nums):
  slow,fast = 0,0
  
  while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
      break
    
  slow2 = 0
  while True:
    slow2 = nums[slow2]
    slow = nums[slow]
    if slow == slow2:
      return slow2
  
    
  return slow

duplicate = find_duplicate([1, 5, 4, 3, 2, 4, 6])
print(duplicate)