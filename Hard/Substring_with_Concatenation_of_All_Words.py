from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        substring_len = word_len * word_count
        word_freq = Counter(words)
        res = []

        for i in range(word_len):
            left = i
            right = i
            curr_freq = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_freq:
                    curr_freq[word] += 1

                    while curr_freq[word] > word_freq[word]:
                        curr_freq[s[left:left + word_len]] -= 1
                        left += word_len

                    if right - left == substring_len:
                        res.append(left)
                else:
                    curr_freq.clear()
                    left = right

        return res
