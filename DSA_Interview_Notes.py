# ==========================================================
# DSA NOTES : Stability & In-Place Sorting
# ==========================================================

# 📌 Stable Sorting
# A sorting algorithm is Stable if equal elements keep their
# original relative order after sorting.
#
# Example:
# Before : [(Prince, 85), (Aman, 85)]
# After  : [(Prince, 85), (Aman, 85)]   ✅ Stable

# 📌 Unstable Sorting
# Equal elements may change their original order.
#
# Example:
# Before : [4A, 2, 4B, 1]
# After  : [1, 2, 4B, 4A]   ❌ Unstable

# ----------------------------------------------------------
# 📌 In-Place Sorting
# ----------------------------------------------------------
# Sorts the array using the same memory.
# Only a few extra variables (i, j, temp, etc.) are used.
#
# Example:
# arr = [5, 2, 4]
# After sorting -> [2, 4, 5]
#
# Extra Space: O(1)

# ----------------------------------------------------------
# 📌 Not In-Place Sorting
# ----------------------------------------------------------
# Uses an additional array or significant extra memory.
#
# Example:
# arr = [5, 2, 4]
# new_arr = sorted(arr)
#
# Extra Space: O(n)

# ==========================================================
# 🚀 Easy Way to Remember
# ==========================================================
#
# Stable      -> Equal elements keep their order.
# Unstable    -> Equal elements may change order.
#
# In-Place    -> Same array + very little extra memory.
# Not In-Place-> Needs another array or significant memory.
#
# ==========================================================
# 🎯 Interview Cheat Sheet
# ==========================================================
#
# Algorithm        Stable      In-Place
# ------------------------------------------
# Bubble Sort        ✅           ✅
# Selection Sort     ❌           ✅
# Insertion Sort     ✅           ✅
# Merge Sort         ✅           ❌
# Quick Sort         ❌           ✅
# Heap Sort          ❌           ✅
#
# ==========================================================