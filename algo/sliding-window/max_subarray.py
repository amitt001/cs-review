"""https://leetcode.com/problems/maximum-subarray/
"""


class Solution:

    def maxSubArray(self, arr):
        max_so_far = current_max = arr[0]
        arr_len = len(arr)

        for i in range(1, arr_len):
            current_max = max(arr[i], current_max + arr[i])
            max_so_far = max(max_so_far, current_max)

        return max_so_far
