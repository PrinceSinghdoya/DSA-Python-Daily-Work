# ==========================================================
# DSA MASTER NOTEBOOK
#
# Topic      : Selection Sort
# Category   : Sorting Algorithms
# Language   : Python
#
# Idea:
# 1. Find the minimum (or maximum) element.
# 2. Swap it with the current index.
# 3. Repeat for the remaining unsorted array.
#
# Time Complexity:
# Best    : O(n²)
# Average : O(n²)
# Worst   : O(n²)
#
# Space Complexity: O(1)
# Stable? : No
# In-place: Yes
#
# ==========================================================



# 1. Find the maximum element.
arr = [29, 10, 14, 37, 13]
class Solution: 
    def selectionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(n):
            max_ind = i
            for j in range(i+1 ,n):
                if arr[j] > arr[max_ind]:
                    max_ind = j
            arr[i], arr[max_ind] = arr[max_ind],arr[i]
        return arr
obj = Solution()
print(obj.selectionSort(arr))



# 2. Find the minimum element.
class Solution: 
    def selectionSort(self, arr):
        # code here
        n = len(arr)
        for i in range(n):
            min_ind = i
            for j in range(i+1 ,n):
                if arr[j] < arr[min_ind]:
                    min_ind = j
            arr[i], arr[min_ind] = arr[min_ind],arr[i]
        return arr
obj = Solution()
print(obj.selectionSort(arr))