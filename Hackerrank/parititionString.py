# Input: nums = [3,5,2,4]
# Output: 2
# Explanation: In the first operation: pick i = 2 and j = 1, the operation is allowed because 2 * nums[2] <= nums[1]. Then mark index 2 and 1.
# It can be shown that there's no other valid operation so the answer is 2.

nums = [1, 78, 27, 48, 14, 86, 79, 68, 77, 20, 57, 21, 18, 67, 5, 51, 70, 85, 47, 56, 22, 79, 41, 8, 39, 81, 59, 74, 14, 45, 49, 15, 10,
        28, 16, 77, 22, 65, 8, 36, 79, 94, 44, 80, 72, 8, 96, 78, 39, 92, 69, 55, 9, 44, 26, 76, 40, 77, 16, 69, 40, 64, 12, 48, 66, 7, 59, 10]
# nums = [3,5,2,4, 1]
# nums = [9, 2, 5, 4, 1]
# nums = [7,6,8]

length = len(nums)
counter = 0
nums.sort()
mid = (length+1)//2
right = mid
left = 0

while left < mid:
  if right < length:
    if 2*nums[left] <= nums[right]:
      counter += 2
      right += 1
      left += 1
    else:
      right += 1
  else:
    break
print(counter)

# totalLen = len(nums)
# counter = 0
# markedIndices = []

# for i in range(totalLen):
#   if i not in markedIndices:
#     for j in range(totalLen):
#       if j not in markedIndices and i not in markedIndices:
#         if i != j:
#           if 2 * nums[i] <= nums[j]:
#             markedIndices.append(i)
#             markedIndices.append(j)
#             # counter += 1

# print(markedIndices)
