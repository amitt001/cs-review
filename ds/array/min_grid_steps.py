"""
https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

You are in an infinite 2D grid where you can move in any of the 8 directions:
(x,y) to (x+1, y), (x - 1, y), (x, y+1), (x, y-1), (x-1, y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points.
Give the minimum number of steps in which you can achieve it. You start from the first point.

Example :

Input : [[3, 1], [3, 2], [2, 2], [1, 2], [0, 2]]
Output : 4

    0   1   2   3
0           y
1           .
2           .
3       x   .

1. Traversal
    1. Start is the index 0 [3, 1]. All other points are destination.
    2. Loop over the array[1:], setting destination x, y = arr[i][0], arr[i][1]. O(n)
    3. While current x != dest x or current y != dest y. O(s)
        - increase or decrease current x based cux x < dest x or current x > dest x. Same for y
        - increase counter
    4. return counter

    s: no of steps, n: input len
    Time: O(n*s), Space: O(1)

2. Distance calculation
    1. Looping over input is required(step 1-2) but while loop is not.
    2. Distance can be calculated using formula: counter += max(abs(cur_x - dst_x), abs(cur_y, dst_y))
    3. cur_x cur_y = dst_x, dst_y
"""


def traversal(inp) -> int:
    counter = 0
    cur_x, cur_y = inp[0]
    for i in inp[1:]:
        dst_x, dst_y = i
        while cur_x != dst_x or cur_y != dst_y:
            if cur_x < dst_x:
                cur_x += 1
            elif cur_x > dst_x:
                cur_x -= 1

            if cur_y < dst_y:
                cur_y += 1
            elif cur_y > dst_y:
                cur_y -= 1

            counter += 1

    return counter


def calculate(inp) -> int:
    counter = 0
    cur_x, cur_y = inp[0]
    for i in inp[1:]:
        dst_x, dst_y = i
        counter += max(abs(cur_x - dst_x), abs(cur_y - dst_y))
        cur_x, cur_y = dst_x, dst_y
    return counter

if __name__ == '__main__':
    inp = [[3, 1], [3, 2], [2, 2], [1, 2], [0, 2]]
    assert traversal(inp) == 4
    assert calculate(inp) == 4
