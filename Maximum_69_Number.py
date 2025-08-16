import time


class Solution:
    """
    You are given a positive integer num consisting only of digits 6 and 9.

    Return the maximum number you can get by changing at most one digit
    (6 becomes 9, and 9 becomes 6).

    Constraints:
        1 <= num <= 10^4
        num consists only of digits 6 and 9.
    """

    def maximum69Number_using_str(self, num: int) -> int:
        """
        Approach:
        - Convert the number to a string to manipulate digits.
        - Replace the first occurrence of '6' with '9' since that gives
          the maximum increase.
        - If no '6' is found, return the original number.
        - Convert back to int and return.
        """
        num_str = list(str(num))
        for i in range(len(num_str)):
            if num_str[i] == "6":
                num_str[i] = "9"
                break
        return int("".join(num_str))

    def maximum69Number_using_int(self, num: int) -> int:
        """
        Approach:
        - Convert the number to a string to manipulate digits.
        - Replace the first occurrence of '6' with '9' since that gives
          the maximum increase.
        - If no '6' is found, return the original number.
        - Convert back to int and return.
        """
        num_str = list(str(num))
        for i in range(len(num_str)):
            if num_str[i] == "6":
                num_str[i] = "9"
                break
        return int("".join(num_str)) 
    


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"num": 9669, "ans": 9969},
        {"num": 9996, "ans": 9999},
        {"num": 9999, "ans": 9999},
        {"num": 6, "ans": 9},
        {"num": 69, "ans": 99},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}

        # str method
        start = time.time()
        ans_str = sol.maximum69Number_using_str(**params)
        end = time.time()
        elapsed_str = (end - start) * 1000

        # int method
        start = time.time()
        ans_int = sol.maximum69Number_using_int(**params)
        end = time.time()
        elapsed_int = (end - start) * 1000

        if ans_str != test_case["ans"]:
            print(
                f"[FAILED: str] Test Case {ind+1} Expected {test_case['ans']}, Got {ans_str}"
            )
        else:
            print(f"[PASSED: str] Test Case {ind+1} (Time: {elapsed_str:.4f} ms)")

        if ans_int != test_case["ans"]:
            print(
                f"[FAILED: int] Test Case {ind+1} Expected {test_case['ans']}, Got {ans_int}"
            )
        else:
            print(f"[PASSED: int] Test Case {ind+1} (Time: {elapsed_int:.4f} ms)")
