# ==========================================================
# DSA MASTER NOTEBOOK
#
# Topic      : Bubble Sort
# Category   : Sorting Algorithms
# Language   : Python
#
# Implementations:
# 1. Bubble Sort (Ascending Order)
# 2. Bubble Sort (Descending Order)
#
# Idea:
# - Compare adjacent elements.
# - Swap them if they are in the wrong order.
# - After each pass, the largest (ascending) or smallest
#   (descending) element reaches its correct position.
# - Repeat until the array is sorted.
#
# Optimization:
# - Use an 'isSwapped' flag.
# - If no swaps occur in a pass, the array is already sorted.
#
# Time Complexity:
# Best    : O(n)   (Already Sorted)
# Average : O(n²)
# Worst   : O(n²)
#
# Space Complexity: O(1)
# Stable? : Yes
# In-place: Yes
#
# ==========================================================



arr = [29, 10, 14, 37, 13]
class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n-2,-1,-1):
            isSwapped = False
            for j in range(0, i+1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    isSwapped = True
            if not isSwapped:
                break
        return arr
obj = Solution()
print(obj.bubbleSort(arr))



class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n-2,-1,-1):
            isSwapped = False
            for j in range(0, i+1):
                if arr[j]<arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    isSwapped = True
            if not isSwapped:
                break
        return arr
obj = Solution()
print(obj.bubbleSort(arr))