import time


class Solution:
    """
    Hercy wants to save money for his first car. He deposits money in the Leetcode bank every day.

    - On the first Monday, he deposits $1.
    - Each following day (Tuesday to Sunday), he deposits $1 more than the previous day.
    - On every subsequent Monday, he deposits $1 more than the *previous Monday*.
      (So the Monday deposits form an arithmetic sequence: 1, 2, 3, ...)

    Given an integer n, return the total amount of money he will have in the bank after n days.

    Example 1:
    -----------
    Input: n = 4
    Output: 10
    Explanation:
      Monday = 1, Tuesday = 2, Wednesday = 3, Thursday = 4 → total = 10

    Example 2:
    -----------
    Input: n = 10
    Output: 37
    Explanation:
      Week 1: 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
      Week 2: 2 + 3 + 4 = 9
      Total = 37

    Example 3:
    -----------
    Input: n = 20
    Output: 96
    Explanation:
      Week 1: 1+2+3+4+5+6+7 = 28
      Week 2: 2+3+4+5+6+7+8 = 35
      Week 3: 3+4+5+6+7+8 = 33
      Total = 28 + 35 + 33 = 96

    Constraints:
    ------------
    1 <= n <= 1000

    Approach:
    ----------
    - Each full week (7 days) forms a clear arithmetic sequence.
      Week 1: start = 1 → sum = 1+2+...+7 = 28
      Week 2: start = 2 → sum = 2+3+...+8 = 35
      Week 3: start = 3 → sum = 3+4+...+9 = 42
    - If n = w * 7 + r (where w = number of full weeks, r = remaining days):
      - Sum full weeks using the arithmetic sum formula.
      - Add remaining days starting from (w + 1).

    Time Complexity: O(1)
    Space Complexity: O(1)
    """

    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remaining_days = n % 7

        # Sum of full weeks:
        # Each week sum = 7 * (2 * start + 6) / 2  => 7 * start + 21
        # start increases from 1 to weeks
        total = (
            weeks * (weeks - 1) * 7 // 2 + weeks * 28
        )  # arithmetic series for starts

        # Remaining days of the next week
        start = weeks + 1
        for i in range(remaining_days):
            total += start + i

        return total


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"n": 4, "ans": 10},
        {"n": 10, "ans": 37},
        {"n": 20, "ans": 96},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.totalMoney(**params)
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
