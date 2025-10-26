import time
from typing import List


class Bank:
    """
    A banking system that supports deposit, withdraw, and transfer operations.

    Each account is numbered from 1 to n, and balances are stored in a 0-indexed list.

    Valid transactions:
    - Accounts involved must exist (1 ≤ account ≤ n).
    - Withdraw or transfer amounts must not exceed available balance.
    """

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def _valid_account(self, account: int) -> bool:
        """Helper to verify if account exists."""
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """
        Transfer money from account1 to account2.

        Returns:
            True if the transfer is valid and successful, else False.
        """
        if not self._valid_account(account1) or not self._valid_account(account2):
            return False
        if self.balance[account1 - 1] < money:
            return False
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        """
        Deposit money into the given account.

        Returns:
            True if the deposit is valid and successful, else False.
        """
        if not self._valid_account(account):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        """
        Withdraw money from the given account.

        Returns:
            True if the withdrawal is valid and successful, else False.
        """
        if not self._valid_account(account):
            return False
        if self.balance[account - 1] < money:
            return False
        self.balance[account - 1] -= money
        return True


class Solution:
    """
    Wrapper class to demonstrate Bank functionality
    in the required format.
    """

    def runBank(self, ops: List[str], params: List[List]) -> List:
        """
        Execute a sequence of operations on the Bank system.

        Approach:
        - Initialize Bank with given balances.
        - For each operation ("withdraw", "transfer", "deposit"), call the respective method.
        - Collect results accordingly.
        """
        output = []
        bank = None

        for op, param in zip(ops, params):
            if op == "Bank":
                bank = Bank(*param)
                output.append(None)
            elif op == "withdraw":
                output.append(bank.withdraw(*param))
            elif op == "transfer":
                output.append(bank.transfer(*param))
            elif op == "deposit":
                output.append(bank.deposit(*param))

        return output


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "ops": ["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"],
            "params": [
                [[10, 100, 20, 50, 30]],
                [3, 10],
                [5, 1, 20],
                [5, 20],
                [3, 4, 15],
                [10, 50],
            ],
            "ans": [None, True, True, True, False, False],
        }
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.runBank(**params)
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
