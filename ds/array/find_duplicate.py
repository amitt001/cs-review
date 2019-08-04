"""
EASY

Given an array of n + 1 integers between 0 and n-1, find one of the duplicates.
If there are multiple possible answers, return one of the duplicates.
If there is no duplicate, return -1.
Example:
Input: [1, 2, 2, 3]
Output: 2
Input: [3, 4, 1, 4, 1]
Output: 4 or 1

Possible solutions:

1. Bruteforce
    for i in range(n-1):
        for j in range(i, n):

    Time: O(n^2), Space: O(1)

2. Using extra space
    - A hashmap(or an array) to store elements
    - If element is already in hashmap, duplicate found.

    Time: O(n), Space: O(n)

3. Sort
    - Sort the array
    - Iterate over each element to check if duplicate
        for i in range(n-1):
            if arr[i] == arr[i+1]:
                return i+1

    Time: O(n(logn)), Space: O(1)

4. Marking [OPTIMAL]
    - This array has an unique property that it contains **1 to n** elements and array size n + 1
    - What that means is we can map each element to it's corresponding index
    - Iterate over array
        - mark(add - sign) to the corresponding index element
    Ex: [3, 4, 1, 4, 1], n = 4
    arr -> [3, 4, 1, 4, 1]
    index-> 0, 1, 2, 3, 4
    i = 3, mark index = 3 -> [3, 4, 1, -4, 1]
    i = 4, mark index = 4 -> [3, 4, 1, -4, -1]
    i = 1, mark index = 1 -> [-3, 4, 1, -4, -1]
    i = 4, mark index = 4 -> already marked, duplicate found

    Time: O(n), Space: O(1)

5. Runner technique(floyd's cycle finding algo) [OPTIMAL]

    - Two variables slow and fast
    - slow = arr[slow], fast = arr[arr[fast]]
    - Keep looping until fast != slow
    Ex: [3, 4, 1, 4, 1]
    slow = arr[0], fast = arr[arr[0]] -> slow = 3, fast = 4
    slow = arr[3], fast = arr[arr[4]] -> slow = 4, fast = 3
    slow = arr[4], fast = arr[arr[3]] -> slow = 1, fast = 1
    Cycle found. Duplicate = 1
"""


# Runner technique
def find_duplicate_floyd(arr):
    # import pdb; pdb.set_trace()
    if not arr or len(arr) <= 1:
        return -1
    slow = arr[0]
    fast = arr[arr[0]]
    # Handle case when arr starts with 0
    if slow == fast:
        return -1
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    return slow


# Mark approach implementation
def find_duplicate(arr):
    tmp_arr = arr[:]
    for e in arr:
        if tmp_arr[e-1] < 0:
            return e
        tmp_arr[e-1] = -(tmp_arr[e-1])
    return -1


if __name__ == '__main__':
    assert find_duplicate([3, 4, 1, 4, 1]) == 4
    assert find_duplicate([1, 2, 2, 3]) == 2
    assert find_duplicate([1, 2]) == -1
    assert find_duplicate([]) == -1
    # Runner
    assert find_duplicate_floyd([3, 4, 1, 4, 1]) == 4
    assert find_duplicate_floyd([1, 2, 2, 3]) == 2
    assert find_duplicate_floyd([0, 1, 2]) == -1
    assert find_duplicate_floyd([]) == -1
