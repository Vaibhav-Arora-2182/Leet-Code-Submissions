import time


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        """
        Find the largest good integer in the given string representation of a number.

        A good integer is defined as:
        - A substring of length 3 in `num`
        - All three characters are the same digit

        Args:
            num (str): The string representing the number.

        Returns:
            str: The largest good integer as a string, or an empty string if none exist.

        Examples:
            >>> sol = Solution()
            >>> sol.largestGoodInteger("6777133339")
            '777'
            >>> sol.largestGoodInteger("2300019")
            '000'
            >>> sol.largestGoodInteger("42352338")
            ''
        """
        for digit in "9876543210":
            triple = digit * 3
            if triple in num:
                return triple
        return ""


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"num": "6777133339", "ans": "777"},  # 777 and 333 → max is 777
        {"num": "2300019", "ans": "000"},  # Only "000"
        {"num": "42352338", "ans": ""},  # No triple
        {"num": "999111222333", "ans": "999"},  # Multiple good integers
        {"num": "000", "ans": "000"},  # Only zeros
    ]

    for ind, test_case in enumerate(test_cases):
        start = time.time()
        params = {k: v for k, v in test_case.items() if k != "ans"}
        ans = sol.largestGoodInteger(**params)
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
