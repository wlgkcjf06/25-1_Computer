def merge_sort(arr):
    print("Splitting into sublists...")
    print(arr)
    if len(arr) < 2:
        return arr
    sp = len(arr) // 2
    left, right = merge_sort(arr[:sp]), merge_sort(arr[sp:])
    # Base case: a list of length 0 or 1 is already sorted
    # Breakdown: split the list into two halves
    # Recursively solve: merge the two sorted halves
    print("Merging of sublists...")
    print(f"{left}, {right}")
    return merge(left, right)
def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    # Merge elements from left and right in sorted order
    # Append any remaining elements from both lists
    return result
lst = [12, 9, 4, 15, 18, 3]
print("Sort via merge function:")
print(merge_sort(lst))
print("Sort via intrinsic function: ")
print(sorted(lst))