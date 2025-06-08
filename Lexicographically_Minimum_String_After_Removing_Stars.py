import heapq
import itertools

class Solution:
    """
    You are given a string s. It may contain any number of '*' characters.
    Your task is to remove all '*' characters.

    While there is a '*', do the following operation:

    Delete the leftmost '*' and the smallest non-'*' character to its left.
    If there are several smallest characters, you can delete any of them.
    Return the lexicographically smallest resulting string after removing all '*' characters.
    """

    def clearStars(self, s: str) -> str:
        if "*" not in s:
            return s
        h = []
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c == "*":
                if not h:
                    continue
                x = h[0]
                if not (v := stacks[x]):
                    continue
                v.pop()
                if not v:
                    heapq.heappop(h)
            else:
                x = ord(c) - 97
                v = stacks[x]
                if not v:
                    heapq.heappush(h, x)
                v.append(i)
        return "".join(s[i] for i in sorted(itertools.chain.from_iterable(stacks)))
