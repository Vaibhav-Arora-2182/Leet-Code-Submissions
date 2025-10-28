import time


class Solution:
    """
    You are given a 0-indexed binary string array 'bank' representing a bank floor plan.
    Each string represents a row of the bank, where:
        - '0' means the cell is empty
        - '1' means there is a security device in that cell

    A laser beam is formed between two devices located in different rows (r1 < r2)
    if all rows between them contain no devices.

    The goal is to return the total number of laser beams in the bank.

    Example:
        Input: bank = ["011001","000000","010100","001000"]
        Output: 8
    """

    def numberOfBeams(self, bank: list[str]) -> int:
        """
        Approach:
        1. For each row, count the number of '1's (devices).
        2. Ignore empty rows (rows with zero devices).
        3. For every consecutive pair of non-empty rows,
           the number of beams formed = devices_in_row1 * devices_in_row2.
        4. Sum up these beams for all valid consecutive pairs.

        Time Complexity: O(m * n)
        Space Complexity: O(1)
        """
        prev_devices = 0
        total_beams = 0

        for row in bank:
            curr_devices = row.count("1")
            if curr_devices > 0:
                total_beams += prev_devices * curr_devices
                prev_devices = curr_devices

        return total_beams


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {"bank": ["011001", "000000", "010100", "001000"], "ans": 8},
        {"bank": ["000", "111", "000"], "ans": 0},
        {"bank": ["1", "0", "1"], "ans": 1},
        {"bank": ["0"], "ans": 0},
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.numberOfBeams(**params)
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
