# N = 5, D = 2
# arr[] = {1,2,3,4,5}
# Output: 3 4 5 1 2
# Explanation: 1 2 3 4 5  when rotated
# by 2 elements, it becomes 3 4 5 1 2.


def rotateArr(arr, rotate, N):
    arr[:] = arr[rotate % N:] + arr[:rotate % N]
    return arr


print(rotateArr([2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 3, 10))
