class Solution:
    """
    Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].
    """

    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, n):
            steps = 0
            first = curr
            last = curr
            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1  # because we're starting from 1

        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr
