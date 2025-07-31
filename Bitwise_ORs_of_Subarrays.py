import time
from typing import List


class Solution:
    """
    Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.

    A subarray is a contiguous non-empty sequence of elements within an array.
    The bitwise OR of a subarray is the bitwise OR of each integer in the subarray.

    Constraints:
    - 1 <= arr.length <= 5 * 10^4
    - 0 <= arr[i] <= 10^9
    """

    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        prev = set()
        for num in arr:
            cur = {num | x for x in prev} | {num}
            result.update(cur)
            prev = cur
        return len(result)

if __name__ == "__main__":
    solution = Solution()
    testcases = [
        {
            "arr": [0],
            "ans": 1,
        },
        {
            "arr": [1, 1, 2],
            "ans": 3,
        },
        {
            "arr": [1, 2, 4],
            "ans": 6,
        },
    ]

    for i, tc in enumerate(testcases):
        params = {k: v for k, v in tc.items() if k != "ans"}
        start = time.time()
        got = solution.subarrayBitwiseORs(**params)
        end = time.time()
        expect = tc["ans"]
        assert got == expect, f"Test case {i+1} failed: got {got}, expected {expect}"
        print(f"Test case - {i} passed in { end - start:.6f} seconds.")
