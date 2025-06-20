from collections import Counter


class Solution:
    """
    You are given a string s consisting of the characters 'N', 'S', 'E', and 'W',
    where s[i] indicates movements in an infinite grid:

        'N' : Move north by 1 unit.
        'S' : Move south by 1 unit.
        'E' : Move east by 1 unit.
        'W' : Move west by 1 unit.

    Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

    Find the maximum Manhattan distance from the origin,
    that can be achieved at any time while performing the movements in order.

    The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
    """

    def maxDistance(self, s: str, k: int) -> int:
        ans = 0

        def opt(a, b, c, d):
            if b < a:
                a, b = b, a
            if a >= k:
                a -= k
                b += k
                rem = 0
            else:
                b += a
                rem = k - a
                a = 0
            if d < c:
                c, d = d, c
            if c >= rem:
                c -= rem
                d += rem
            else:
                d += c
                c = 0
            return (b - a) + (d - c)

        a1 = a2 = a3 = a4 = 0
        for ch in s:
            if ch == "E":
                a1 += 1
            elif ch == "W":
                a2 += 1
            elif ch == "N":
                a3 += 1
            else:
                a4 += 1
            ans = max(ans, opt(a1, a2, a3, a4))
        return ans
