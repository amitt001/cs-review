"""Complexity O(n^3)

[1, -3, 5, -6, -2]
[1, 0, 5, 0, 0]
[5, -6, 7, -1, 1, 3, 12, -7]
[5,  0, 7, 6, 7, 10, 22,  0]
"""

import sys
import json


class Solution:

    def maxSubArray(self, arr):
        # O(n^3)
        max_so_far = -sys.maxsize - 1
        arr_len = len(arr)

        for i in range(arr_len):    # O(n)
            for j in range(arr_len - i):    # O(n)
                sum_val = sum(arr[j:j+i+1])     # O(n)
                if sum_val > max_so_far:
                    max_so_far = sum_val
        return max_so_far

    def maxSubArrayImproved(self, arr):
        # O(n^2)
        max_so_far = -sys.maxsize - 1
        arr_len = len(arr)

        for start_index in range(arr_len):  # O(n)
            sum_val = 0
            for step in range(arr_len - start_index):   # O(n)
                # Improvement from brute force. Instead of adding
                # all the values, we add last calculated sum_val + current index.
                sum_val += arr[start_index + step]
                if sum_val > max_so_far:
                    max_so_far = sum_val
        return max_so_far

    def maxSubArrayDP(self, arr):
        # Kadane’s Algorithm, O(N), Dynamic Programming
        max_so_far = current_max = arr[0]
        arr_len = len(arr)

        for i in range(1, arr_len):
            current_max = max(arr[i], current_max + arr[i])
            max_so_far = max(max_so_far, current_max)

        return max_so_far

    def maxSubArrayDivideAndConquer(self, arr):
        """Like merge sort,
            1. Get the max sum from the left half
            2. Get the max sum from the right half
            3. Get the max sum from crossing of two halves and return the sum of two

        Return the max of the three

        O(nlogn)
        """

        def max_crossing_sum(arr, l, m, h):
            sm = 0
            left_sum = - sys.maxsize - 1
            for i in range(m, l-1, -1):
                sm += arr[i]
                if sm > left_sum:
                    left_sum = sm

            sm = 0
            right_sum = - sys.maxsize - 1
            for j in range(m + 1, h + 1):
                sm += arr[j]
                if sm > right_sum:
                    right_sum = sm

            return left_sum + right_sum

        def max_subarray(arr, l, h):
            # Base case
            if l == h:
                return arr[l]

            m = (l + h) // 2

            return max(
                max_subarray(arr, l, m),
                max_subarray(arr, m + 1, h),
                max_crossing_sum(arr, l, m, h))

        return max_subarray(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    input_arr = json.loads(input())
    print(Solution().maxSubArrayDivideAndConquer(input_arr))
