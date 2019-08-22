"""Given an array, rotate the array to the right by k steps, where k is non-negative.

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]

- Using shifting
    - Shift last k characters to the beginning to arr
    - Shift first `d = arr_len - k` d characters to the last d characters

Time: O(n), Space: O(d)?
"""


def rotate(nums, k) -> None:
    l = len(nums)
    if l in [0, 1]:
        return nums
    k = k % l
    d = l - k
    # Shift len - k characters to the left and move first d characters to the right
    nums[:] = nums[d:] + nums[:d]


def smart_rotate(nums, k):
    """Intentionally using actual array rotation instead of Python's
    internal reversed
    Time: O(n), space: O(1)
    """
    l = len(nums)
    if l in [0, 1]:
        return
    k = k % l
    counter = l - k - 1
    for i in range((l - k)//2):
        nums[i], nums[counter] = nums[counter], nums[i]
        counter -= 1


    counter = l - 1
    for i in range((k)//2):
        nums[l - k + i], nums[counter] = nums[counter], nums[l - k + i]
        counter -= 1

    counter = l - 1
    for i in range(l//2):
        nums[i], nums[counter] = nums[counter], nums[i]
        counter -= 1


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]
    nums = [1, 2, 3, 4, 5]
    smart_rotate(nums, 15)
    assert nums[0] == 1

    nums = [1, 2, 3, 4, 5]
    smart_rotate(nums, 3)
    assert nums[0] == 3

    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    assert nums[0] == 5
    assert nums[-1] == 4
