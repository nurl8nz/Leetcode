from itertools import combinations
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, combinations(range(1, n + 1), k)))
