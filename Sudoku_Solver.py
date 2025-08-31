import time


class Solution:
    """
    Write a program to solve a Sudoku puzzle by filling the empty cells.

    A sudoku solution must satisfy all of the following rules:
    - Each row must contain the digits 1-9 without repetition.
    - Each column must contain the digits 1-9 without repetition.
    - Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    The '.' character indicates empty cells.
    """

    def solveSudoku(self, board: list[list[str]]) -> list[list[str]]:
        """
        Approach:
        - Use backtracking with bitmask optimization.
        - Maintain three arrays of bitmasks: one for rows, one for columns, and one for boxes.
        - Each mask tracks which digits are already used.
        - For every empty cell, try placing valid digits (1-9).
        - If no digit fits, backtrack.
        - This ensures efficient constraint checking in O(1) time.
        - Guaranteed to find a unique valid solution.
        """

        row_mask = [0] * 9
        col_mask = [0] * 9
        box_mask = [0] * 9
        empties = []

        def get_box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        # initialize masks
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    d = int(board[r][c])
                    bit = 1 << d
                    row_mask[r] |= bit
                    col_mask[c] |= bit
                    box_mask[get_box_id(r, c)] |= bit

        def backtrack(idx=0) -> bool:
            if idx == len(empties):
                return True  # solved!

            r, c = empties[idx]
            b = get_box_id(r, c)

            used = row_mask[r] | col_mask[c] | box_mask[b]
            for d in range(1, 10):
                bit = 1 << d
                if not (used & bit):
                    # place digit
                    board[r][c] = str(d)
                    row_mask[r] |= bit
                    col_mask[c] |= bit
                    box_mask[b] |= bit

                    if backtrack(idx + 1):
                        return True

                    # undo
                    board[r][c] = "."
                    row_mask[r] ^= bit
                    col_mask[c] ^= bit
                    box_mask[b] ^= bit

            return False

        backtrack()
        return board


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "board": [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            "ans": [
                ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
            ],
        },
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}

        start = time.time()
        ans = sol.solveSudoku(**params)
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
