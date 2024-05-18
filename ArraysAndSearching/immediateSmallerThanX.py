# N = 5
arr = [1,2,3,4,5]
# arr.sort()
X = 1
# Output: 15


def findImmediateSmaller(arr, output_elem, X):
    min_diff = 100000000000000000
    for elem in arr:
        if elem < X:
            if min_diff > X-elem:
                min_diff = X - elem
                output_elem = elem
    return output_elem

print(findImmediateSmaller(arr, -1, X))
