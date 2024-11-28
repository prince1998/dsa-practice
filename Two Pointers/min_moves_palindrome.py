def min_moves_to_make_palindrome(s):
  s = list(s)
  moves = 0
  i = 0
  j = len(s)-1
  while i < j:
      k = j
      while k > i:
        if s[k] == s[i]:
          l = k
          while l < j:
            s[l], s[l+1] = s[l+1],s[l]
            moves+=1
            l+=1
          j-=1
          break
        k-=1
      if k == i:
        moves+=len(s)//2-i
      i+=1
  return moves


moves = min_moves_to_make_palindrome("ccxx")
print(moves)