import math
import operator
import re
import string
from bisect import bisect_left, bisect_right
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import (ceil, comb, exp, gcd, inf, isqrt, lcm, log, log2, log10,
                  perm, prod, sqrt)
from typing import *

import pytest

from .binary_tree import *


class Solution:
    """Implement your method here."""

    def add2(self, a, b):
        return a + b


functions = [(k, v) for k, v in vars(Solution).items() if not k.startswith('_') and callable(v)]
assert len(functions) == 1, f'class Solution should have exact 1 API method, got {len(functions)}: {functions}'
fun = getattr(Solution(), functions[0][0])


@pytest.mark.parametrize('args, kwargs, want', [
    # paste the outputs of `gen_testcases.py` here
    ((2, 3,), {}, 5),
    ((4, -6,), {}, -2),
    ((-4, -6,), {}, -10),
    ((0, 1,), {}, 1),
    ((-3, 8,), {}, 5),
])
def test(args, kwargs, want):
    got = fun(*args, **kwargs)
    if isinstance(got, float):
        assert got == pytest.approx(want)
    elif isinstance(got, TreeNode):
        if isinstance(want, list):
            assert bitree2list(got) == want
        else:
            assert got.val == want
    else:
        assert fun(*args, **kwargs) == want

# if __name__=='__main__':
#     print()
