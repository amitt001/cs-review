
def longest_palindrom_subs(s):
    if len(s) < 2:
        return s or ""
    max_subs = s[0]
    max_len = 1
    for i in range(1, len(s)):
        mid = i // 2
        print(s[mid], i)
        if i % 2 == 1:
            if s[mid] != s[mid-1]:
                continue
        tmp = s[mid]
        index = 1
        while mid-index > 0 and mid+index < len(s) - 1 and (s[mid-index] == s[mid + index]):
            tmp = s[index-1] + tmp + s[index + 1]
            index += 1
        if len(tmp) > max_len:
            max_len = len(tmp)
            max_subs = tmp

    return max_subs



if __name__ == '__main__':
    s = "abcdcef"
    print(longest_palindrom_subs(s))
