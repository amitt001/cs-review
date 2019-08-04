"""Longest common subsequence

"X = "ABCBDAB" and Y = "BDCABA", the LCS(X, Y) = {"BCBA", "BDAB", "BCAB"}"

    {   if X[i] == Y[j], lcs[i][j] = 1 + lcs[i-1][j-1])
T = {
    {   if X[i] != Y[j], lcs = max(lcs[i-1][j], lcs[i][j-1])

Example:
    s1 = ABC, s2 = DBC
    reversed_substr = ''
    lcs_arr = []
          A  B  C
      [0][0][0][0]
    D [0][0][0][0]
    B [0][0][1][1]
    C [0][0][1][2] |
               ---

To get the sequence:
    1. Start from the max of the lcs_arr
    2. If lcs_arr[3][3] != lcs_arr[3-1][3] and lcs_arr[3][3-1]
        2.1 reversed_substr += s1[3-1]
        2.2 move to lcs_arr[2][2] and repeat 2.1 and 2.2
        2.3 print(reversed(reversed_substr))
    3. if lcs_arr[3][3] == lcs_arr[3-1][3]
        3.1 move to lcs_arr[3-1][3] and repeat 2 and 3
    4. if lcs_arr[3][3] == lcs_arr[3][3-1]
        4.1 move to lcs_arr[3][3-1] and repeat 2 and 3

NOTE:
1. Be careful with which substring is used as row of DP array and which one is used as col
2. DP arr is one size larger than the string lengths
3. Lots of chances of index error
"""


def lcs(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 == 0 or len_s2 == 0:
        return 0

    lcs_arr = [[0 for i in range(len_s1 + 1)] for i in range(len_s2 + 1)]

    for i in range(1, len_s2 + 1):
        for j in range(1, len_s1 + 1):
            if s1[j-1] == s2[i-1]:
                lcs_arr[i][j] = 1 + lcs_arr[i-1][j-1]
            else:
                lcs_arr[i][j] = max(lcs_arr[i-1][j], lcs_arr[i][j-1])

    # Print the subsequence
    print_subseq(lcs_arr, s1, s2)

    print(lcs_arr[i][j])


def print_subseq(lcs_arr, s1, s2):
    substr = ''
    row, col = len(s2), len(s1)

    while row > 0 and col > 0:
        if lcs_arr[row][col] == lcs_arr[row-1][col]:
            row -= 1
        elif lcs_arr[row][col] == lcs_arr[row][col-1]:
            col -= 1
        else:
            row -= 1
            col -= 1
            substr += s2[row]
    print(substr[::-1])



if __name__ == '__main__':
    lcs('BBA', 'ABCBDABVAA')
