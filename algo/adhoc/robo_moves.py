"""
Check if a given sequence of moves for a robot is circular or not.

G - Go one unit
L - Turn left
R - Turn right 

Input: path[] = "GLGLGLG"
Output: CIRCULAR

Trick is to use a two-value tuple and start from (0, 0). If back to (0,0) -> circular
"""


def check_circular(s):
    # 0 -> north, 1 -> west, 2 -> south, 3 -> east
    direction = 0
    # (x, y)
    start = current = (0, 0)
    for i in s:
        if i in ['L', 'R']:
            direction = (direction + 1) % 4
        else:
            if direction == 0:
                current = current[0], current[1] + 1
            elif direction == 1:
                current = current[0] - 1, current[1]
            elif direction == 2:
                current = current[0], current[1] - 1
            else:
                current = current[0] + 1, current[1]

    return 'CIRCULAR' if start == current else 'NOT'


if __name__ == '__main__':
    assert check_circular('GLGLGLG') == 'CIRCULAR'
    assert check_circular('GLLG') == 'CIRCULAR'
    assert check_circular('GLLGLG') == 'NOT'
