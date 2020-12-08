class Solution:
    def lengthOfLongestSubstring(self, s):
        window = {}
        for c in s:
            window[c] = 0
        left, right = 0, 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1

            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right-left)
        return res

if __name__=='__main__':
    s = "abcabcbb"  # 3
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)
