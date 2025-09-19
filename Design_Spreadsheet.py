import time


class Spreadsheet:
    def __init__(self, rows: int):
        """
        Initializes a spreadsheet with 26 columns and the given number of rows.
        All cells are initially set to 0.
        """
        self.sheet: dict[str, int] = {}

    def setCell(self, cell: str, value: int) -> None:
        """
        Sets the value of a cell.
        """
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        """
        Resets the specified cell to 0.
        """
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        """
        Evaluates a formula of form '=X+Y'.
        X, Y are either integers or cell references.
        """
        x, y = formula[1:].split("+")
        return self.resolve(x) + self.resolve(y)

    def resolve(self, token: str) -> int:
        if token.isdigit():
            return int(token)
        return self.sheet.get(token, 0)


if __name__ == "__main__":
    spreadsheet = Spreadsheet(3)

    test_cases = [
        {"func": "getValue", "args": ["=5+7"], "ans": 12},
        {"func": "setCell", "args": ["A1", 10], "ans": None},
        {"func": "getValue", "args": ["=A1+6"], "ans": 16},
        {"func": "setCell", "args": ["B2", 15], "ans": None},
        {"func": "getValue", "args": ["=A1+B2"], "ans": 25},
        {"func": "resetCell", "args": ["A1"], "ans": None},
        {"func": "getValue", "args": ["=A1+B2"], "ans": 15},
    ]

    for ind, test in enumerate(test_cases):
        func = getattr(spreadsheet, test["func"])
        start = time.time()
        result = func(*test["args"])
        end = time.time()
        elapsed_ms = (end - start) * 1000

        if result != test["ans"]:
            print(
                f"Test Case - {ind + 1} FAILED\n"
                f"Expected: {test['ans']}, Got: {result}\n"
                f"Test = {test} "
                f"(Time: {elapsed_ms:.4f} ms)\n"
            )
        else:
            print(f"Test Case - {ind + 1} PASSED (Time: {elapsed_ms:.4f} ms)")
