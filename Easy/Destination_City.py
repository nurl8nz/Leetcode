from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = set(cityA for cityA, cityB in paths)
        for cityA, cityB in paths:
            if cityB not in outgoing:
                return cityB
