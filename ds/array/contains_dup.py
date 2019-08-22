"""Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Input: [1,2,3,1]
Output: true

Input: [1,2,3,4]
Output: false
"""


def containsDuplicate(nums) -> bool:
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False


def sol_const_space(nums) -> bool:
    if not nums:
        return
    nums.sort()
    last_val = nums[0]
    for i in nums[1:]:
        if i == last_val:
            return True
        last_val = i
    return False


if __name__ == '__main__':
    arr = [1, 2, 3, 1]
    assert containsDuplicate(arr) is True
    assert sol_const_space(arr) is True

    arr = [1, 2, 3, 4]
    assert containsDuplicate(arr) is False
    assert sol_const_space(arr) is False
