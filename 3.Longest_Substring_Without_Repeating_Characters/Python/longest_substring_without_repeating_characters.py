class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hash_dict = {}
        ans = 0
        i = 0
        for j in range(n):
            if s[j] in hash_dict:
                i = max(hash_dict[s[j]], i)
            ans = max(ans, j - i + 1)
            hash_dict[s[j]] = j + 1
        return ans