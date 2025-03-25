class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(start, target, current):
            if target == 0:
                result.append(list(current))
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    current.append(candidates[i])
                    backtrack(i, target - candidates[i], current)
                    current.pop()
        
        backtrack(0, target, [])
        return result
