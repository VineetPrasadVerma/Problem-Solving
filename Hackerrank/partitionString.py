# Input: s = "165462", k = 60
# Output: 4
# Explanation: We can partition the string into substrings "16", "54", "6", and "2". Each substring has a value less than or equal to k = 60.
# It can be shown that we cannot partition the string into less than 4 substrings.


def minimumPartition(s, k):
  length = len(s)
  counter = 0
  left = 0

  temp = s[left]
  for i in s:
    if int(i) > k:
      return -1
  
  while left < length:
    print(left, temp)
    if int(temp) <= k:
      if len(temp) == 1 or left == length - 1:
        if int(temp) <= k:
          counter += 1
          break
      else:
        left += 1
        temp += s[left]
    else:
      counter += 1
      print('cc', counter)
      temp = s[left]
  print('c', counter)
      
minimumPartition('2995624428278123422153476983795874268215311982758939386251', 128)
        