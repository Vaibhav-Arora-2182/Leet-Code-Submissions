import time
from collections import defaultdict
from typing import Dict, List


class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.serial: str = ""
        self.delete: bool = False


class Solution:
    """
    Due to a bug, there are many duplicate folders in a file system.
    You are given a 2D array `paths`, where paths[i] is an array representing an absolute path to the ith folder.

    For example, ["one", "two", "three"] represents the path "/one/two/three".

    Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical
    subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical.
    If two or more folders are identical, then mark the folders as well as all their subfolders.

    Example of duplicate:
    /a
    /a/x
    /a/x/y
    /a/z
    /b
    /b/x
    /b/x/y
    /b/z

    If path "/b/w" were added, then /a and /b would not be identical.
    However, /a/x and /b/x would still be identical.

    The system only deletes all marked folders once, so any folders that become identical after deletion are not deleted.

    Return a 2D array of remaining folders after deletion. Order does not matter.
    """

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()

        # Build Trie
        for path in paths:
            curr = root
            for folder in path:
                if folder not in curr.children:
                    curr.children[folder] = TrieNode()
                curr = curr.children[folder]

        serial_count = defaultdict(int)

        # Post-order serialize subtree
        def serialize(node: TrieNode) -> str:
            if not node.children:
                return ""

            items = []
            for name in sorted(node.children):
                child = node.children[name]
                child_serial = serialize(child)
                items.append(f"{name}({child_serial})")
            node.serial = "".join(items)
            serial_count[node.serial] += 1
            return node.serial

        serialize(root)

        # Mark nodes to delete
        def mark_deletions(node: TrieNode):
            for name, child in node.children.items():
                mark_deletions(child)
                if child.serial and serial_count[child.serial] > 1:
                    child.delete = True

        mark_deletions(root)

        # Collect paths if not marked for deletion
        res = []

        def collect_paths(node: TrieNode, path: List[str]):
            for name, child in node.children.items():
                if not child.delete:
                    new_path = path + [name]
                    res.append(new_path)
                    collect_paths(child, new_path)

        collect_paths(root, [])
        return res


# Test cases and runner
if __name__ == "__main__":
    testcases = {
        "Example 1": {
            "paths": [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]],
            "ans": [["d"], ["d", "a"]],
        },
        "Example 2": {
            "paths": [
                ["a"],
                ["c"],
                ["a", "b"],
                ["c", "b"],
                ["a", "b", "x"],
                ["a", "b", "x", "y"],
                ["w"],
                ["w", "y"],
            ],
            "ans": [["a"], ["a", "b"], ["c"], ["c", "b"]],
        },
        "Example 3": {
            "paths": [["a", "b"], ["c", "d"], ["c"], ["a"]],
            "ans": [["a"], ["a", "b"], ["c"], ["c", "d"]],
        },
    }

    solution = Solution()
    for name, tc in testcases.items():
        start = time.perf_counter()
        params = {k: v for k, v in tc.items() if k != "ans"}

        result = solution.deleteDuplicateFolder(**params)
        end = time.perf_counter()

        expected = tc["ans"]
        result_set = {tuple(x) for x in result}
        expected_set = {tuple(x) for x in expected}

        assert (
            result_set == expected_set
        ), f"{name} failed:\nExpected: {expected_set}\nGot: {result_set}"
        print(f"{name} passed in {(end - start) * 1000:.3f} ms.")
