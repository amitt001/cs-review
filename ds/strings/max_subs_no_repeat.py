"""
Given a string of characters, find the maximum substring with no repetitions.

Q. How large string can be? What to return bool or string itself. What to return in case of multiple?

1. Brute force
    - Loop over the string while also storing the chars in hashmap with bool value
    - Check if a duplicate found
    - If duplicate found check if current string pattern len > current max pattern and set the value
    - start looping from start + 1
    - Repeat above steps

    Time: O(n^2), space: O(n)

2. Hash map with char position
    - Loop over string while storing the char and it's position in the string as value
    - Set start = 0 and end = 0 initally and start incrementing end
    - If duplicate found, check max len till now if end - star > current_max
        - save char_stringstart:end]
        - start = map[key]
    - repeat

    Time: O(n), Space: O(n)
"""

def max_unique_subs(s):
    if not s:
        return ""

    max_len = 0
    subs = ""
    # Space: O(n)
    char_map = {}
    start, end = 0, 0

    # O(n) -> one iteration
    for idx, i in enumerate(s):
        if i in char_map:
            if max_len < (end - start):
                subs = s[start:end]
                max_len = (end - start)
            start = char_map[i] + 1

        end += 1
        char_map[i] = idx
    return subs


if __name__ == '__main__':
    assert max_unique_subs("abcdazck") == "bcdaz"

