import time
from itertools import permutations


class Solution:
    """
    An integer x is numerically balanced if for every digit d in x,
    there are exactly d occurrences of that digit in x.

    Given an integer n, return the smallest numerically balanced number
    strictly greater than n.

    Example 1:
    -----------
    Input: n = 1
    Output: 22
    Explanation:
      - 22 is numerically balanced since the digit '2' occurs 2 times.
      - It is also the smallest numerically balanced number > 1.

    Example 2:
    -----------
    Input: n = 1000
    Output: 1333
    Explanation:
      - 1333 is numerically balanced since:
          * '1' occurs 1 time
          * '3' occurs 3 times
      - It is the smallest numerically balanced number > 1000.

    Example 3:
    -----------
    Input: n = 3000
    Output: 3133
    Explanation:
      - 3133 is numerically balanced since:
          * '1' occurs 1 time
          * '3' occurs 3 times
      - It is the smallest numerically balanced number > 3000.

    Constraints:
    ------------
    0 <= n <= 10^6

    Approach:
    ----------
    - All numerically balanced numbers are quite rare and bounded (since their digits count
      and pattern are small). We can precompute all possible numerically balanced numbers by:
        1. Defining small “base” patterns like "22", "122", "333", "1333", etc.
        2. Generating all unique permutations of these base strings.
        3. Converting them to integers and sorting them.
    - Once precomputed, we simply iterate through this sorted list to find the
      smallest number greater than n.

    Time Complexity:
    ----------------
    Precomputation: O(P) where P is the total number of generated permutations (small constant).
    Query: O(len(balanced_numbers)) ≈ O(1) since it’s a small list.

    Space Complexity:
    -----------------
    O(P) for storing all balanced numbers.
    """

    balanced_numbers = None

    @staticmethod
    def init_balanced_numbers():
        s = set()
        bases = [
            "1",
            "22",
            "122",
            "333",
            "1333",
            "4444",
            "14444",
            "22333",
            "55555",
            "122333",
            "155555",
            "224444",
            "666666",
            "1224444",
            "1666666",
            "2255555",
            "3334444",
            "7777777",
            "12255555",
        ]

        for base in bases:
            for p in set(permutations(sorted(base))):
                s.add(int("".join(p)))
        return sorted(s)

    def __init__(self):
        if Solution.balanced_numbers is None:
            Solution.balanced_numbers = Solution.init_balanced_numbers()

    def nextBeautifulNumber(self, n: int) -> int:
        for x in Solution.balanced_numbers:
            if x > n:
                return x
        return -1


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 1, "ans": 22},
        {"n": 1000, "ans": 1333},
        {"n": 3000, "ans": 3133},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.nextBeautifulNumber(**params)
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if ans != test_case["ans"]:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {test_case['ans']}, Got: {ans}\n"
                f"Test Case = {test_case} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
