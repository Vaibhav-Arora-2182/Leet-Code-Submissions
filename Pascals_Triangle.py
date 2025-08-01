import time
from typing import List


class Solution:
    """
    Given an integer numRows, return the first numRows of Pascal's triangle.

    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
    """

    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for _ in range(numRows - 1):
            prev = out[-1]
            x = [prev[j] + prev[j + 1] for j in range(len(prev) - 1)]
            new = [1] + x + [1]
            out.append(new)
        return out


if __name__ == "__main__":
    solution = Solution()
    testcases = [
        {
            "numRows": 5,
            "ans": [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        },
        {
            "numRows": 1,
            "ans": [[1]],
        },
        {
            "numRows": 2,
            "ans": [[1], [1, 1]],
        },
        {
            "numRows": 3,
            "ans": [[1], [1, 1], [1, 2, 1]],
        },
    ]

    for i, tc in enumerate(testcases):
        params = {k: v for k, v in tc.items() if k != "ans"}
        start = time.time()
        got = solution.generate(**params)
        end = time.time()
        expect = tc["ans"]
        assert got == expect, f"Test case {i+1} failed: got {got}, expected {expect}"
        print(f"Test case - {i} passed in {end - start:.6f} seconds.")
