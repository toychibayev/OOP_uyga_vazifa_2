class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        unli = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        current_count = 0
        for i in range(k):
            if s[i] in unli:
                current_count += 1
            
        count = current_count
        for i in range(k, len(s)):
            if s[i] in unli:
                current_count += 1
            if s[i - k] in unli:
                current_count -= 1
            count = max(count, current_count)
        return count
        