# Given a string num_str representing a palindrome, the string only contains digits. Your task is to return the next possible palindrome using the same digits. The returned palindrome would be the next largest palindrome, meaning there can be more than one way to rearrange the digits to make a larger palindrome. Return an empty string if no greater palindrome can be made.

# Consider the following example to understand the expected output for a given numeric string:

# input string = "123321"

# possible palindromes = "213312", "231132", "312213", "132231", "321123"

# We should return the palindrome "132231" as it is greater than "123321" yet the smallest palindrome excluding the original palindrome


def find_next_palindrome(num_str):
  num_str_list = list(num_str)
  length_of_str = len(num_str)
  if length_of_str == 1:
    return ""

  else:
    left_half = num_str_list[0:length_of_str//2]
    
    # for i in range((length_of_str//2)-2,0,-1):
    #   if int(left_half[i]) < int(left_half[i+1]):
   
    #     for j in range((length_of_str//2)-1,i,-1):
    #       if int(left_half[j]) > int(left_half[i]):
    #         min_large = left_half[j]
    #         if int(min_large) <= int(left_half[j]):
    #           min_large = left_half[j]
    #           min_large_index = j
    #     left_half[i],left_half[min_large_index] = left_half[min_large_index],left_half[i]
    #     left_half[i + 1:] = reversed(left_half[i + 1:])
    #     break
    i = len(left_half) - 2
    while i >= 0 and left_half[i] >= left_half[i + 1]:
      i -= 1
    if i == -1:
      return ""

    # Step 2: Find the next largest digit to swap with digits[i]
    j = len(left_half) - 1
    while left_half[j] <= left_half[i]:
      j -= 1
      
    left_half[i], left_half[j] = left_half[j], left_half[i]
    left_half[i + 1:] = reversed(left_half[i + 1:])

    right_half = left_half[::-1]
    if length_of_str % 2 != 0:
      middle_char = num_str_list[length_of_str//2]
      middle_char = list(middle_char)
      final_list = left_half+middle_char+right_half
      final_string = "".join(final_list)
      if final_string <= num_str:
        final_string = ""
    else:
      final_list = left_half+right_half
      final_string = "".join(final_list)
      if final_string <= num_str:
        final_string = ""
    return final_string

print(find_next_palindrome("12321"))