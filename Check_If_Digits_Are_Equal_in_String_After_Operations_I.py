import time


class Solution:
    """
    You are given a string `s` consisting of digits.

    Perform the following operation repeatedly until the string has exactly two digits:
      - For each pair of consecutive digits in `s`, starting from the first digit,
        calculate a new digit as the sum of the two digits modulo 10.
      - Replace `s` with the sequence of newly calculated digits, maintaining the order
        in which they are computed.

    Return True if the final two digits in `s` are the same; otherwise, return False.

    Example 1:
    -----------
    Input: s = "3902"
    Output: True

    Explanation:
      Step 1: (3+9)%10=2, (9+0)%10=9, (0+2)%10=2 → s = "292"
      Step 2: (2+9)%10=1, (9+2)%10=1 → s = "11"
      Since both digits are equal, return True.

    Example 2:
    -----------
    Input: s = "34789"
    Output: False

    Explanation:
      Step 1: "34789" → "7157"
      Step 2: "7157" → "862"
      Step 3: "862" → "48"
      Since 4 != 8, return False.

    Constraints:
    ------------
    - 3 <= len(s) <= 100
    - s consists only of digits ('0'–'9')

    Time Complexity: O(n²) in the worst case (length reduces by 1 each iteration)
    Space Complexity: O(n)
    """

    def hasSameDigits(self, s: str) -> bool:
        while (int(s) // 100) > 0:  
            new = ""
            for ind in range(len(s) - 1):
                new += str((int(s[ind]) + int(s[ind + 1])) % 10)
            s = new
        return s[0] == s[1]


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"s": "3902", "ans": True},
        {"s": "34789", "ans": False},
        {"s": "141", "ans": True},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.hasSameDigits(**params)
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
