class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, max_len = [-1], 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len
