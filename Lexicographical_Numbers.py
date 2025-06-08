from typing import List


class Solution:
    """
    Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

    You must write an algorithm that runs in O(n) time and uses O(1) extra space.
    """

    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1
        for _ in range(n):
            res.append(curr)
            if curr * 10 <= n:
                # Go deeper (Trie child)
                curr *= 10
            else:
                # Go to next sibling or backtrack
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1
        return res
