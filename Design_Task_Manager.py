import heapq
import time
from typing import Dict, List, Tuple


class TaskManager:
    """
    A task management system that supports adding, editing, removing,
    and executing tasks by priority.

    Each task is defined by (userId, taskId, priority).
    - execTop executes the task with the highest priority.
      If multiple tasks share the same priority, the one with the higher taskId is chosen.
    """

    def __init__(self, tasks: List[List[int]]):

        self.task_map: Dict[int, Tuple[int, int]] = {}
        self.heap: List[Tuple[int, int, int]] = []

        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, neg_taskId, userId = heapq.heappop(self.heap)
            taskId = -neg_taskId
            if taskId in self.task_map and self.task_map[taskId] == (userId, -priority):
                del self.task_map[taskId]
                return userId
        return -1


class Solution:
    """
    Wrapper class to demonstrate TaskManager functionality
    in the required format.
    """

    def runTaskManager(self, ops: List[str], params: List[List]) -> List:
        """
        Execute a sequence of operations on TaskManager.

        Approach:
        - Initialize TaskManager with given tasks.
        - For each operation ("add", "edit", "rmv", "execTop"), call the corresponding method.
        - Collect results where needed (None for void methods).
        """
        output = []
        taskManager = None

        for op, param in zip(ops, params):
            if op == "TaskManager":
                taskManager = TaskManager(*param)
                output.append(None)
            elif op == "add":
                taskManager.add(*param)
                output.append(None)
            elif op == "edit":
                taskManager.edit(*param)
                output.append(None)
            elif op == "rmv":
                taskManager.rmv(*param)
                output.append(None)
            elif op == "execTop":
                output.append(taskManager.execTop())

        return output


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        {
            "ops": ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"],
            "params": [
                [[[1, 101, 10], [2, 102, 20], [3, 103, 15]]],
                [4, 104, 5],
                [102, 8],
                [],
                [101],
                [5, 105, 15],
                [],
            ],
            "ans": [None, None, None, 3, None, None, 5],
        }
    ]

    for ind, test_case in enumerate(test_cases):
        params = {k: v for k, v in test_case.items() if k != "ans"}
        start = time.time()
        ans = sol.runTaskManager(**params)
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
