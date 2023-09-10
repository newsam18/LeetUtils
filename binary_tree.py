"""LeetCode style of representation of Binary Tree."""

from typing import Final
from collections import deque

__all__ = ('TreeNode', 'null', 'list2bitree', 'bitree2list')

null: Final = None


class TreeNode:
    """LeetCode definition of Binary Tree."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if self.left is None and self.right is None:
            return f'T[{self.val}]'
        left = '~' if self.left is None else str(self.left)
        right = '~' if self.right is None else str(self.right)
        return f'T[{self.val}, {left}, {right}]'


def list2bitree(a: list) -> TreeNode | None:
    if not a:
        return None
    root = TreeNode(a[0])
    q = deque([root])
    i, n = 1, len(a)
    while q:
        node: TreeNode = q.popleft()
        # left
        if i >= n:
            break
        if a[i] is not None:
            node.left = TreeNode(a[i])
            q.append(node.left)
        i += 1
        # right
        if i >= n:
            break
        if a[i] is not None:
            node.right = TreeNode(a[i])
            q.append(node.right)
        i += 1
    return root


def bitree2list(root: TreeNode | None) -> list:
    if not root:
        return []
    q = deque([root])
    ans = []
    while q:
        x: TreeNode | None = q.popleft()
        if not x:
            ans.append(None)
            continue
        ans.append(x.val)
        q.append(x.left)
        q.append(x.right)
    while ans and ans[-1] is None:
        ans.pop()
    return ans


if __name__ == '__main__':
    for a in [
        [],
        [2],
        [1, 3, null, null, 2],
        [3, 1, 4, null, null, 2],
        [3, 1, 4, None, None, None, 2, 5],
    ]:
        root = list2bitree(a)
        print(root)
        b = bitree2list(root)
        assert a == b, (a, b)
    print('Test TreeNode ok.')
