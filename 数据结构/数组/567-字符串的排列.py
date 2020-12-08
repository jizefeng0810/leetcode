class Solution:
    def checkInclusion(self, s1: str, s2: str):
        need, window = {}, {}
        for c in s1:
            window[c] = 0
            if c in need.keys():
                need[c] += 1
            else:
                need[c] = 1
        left, right = 0, 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need.keys():
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                if d in need.keys():
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False

if __name__=='__main__':
    s1 = "ab"
    s2 = "eidbaooo"           # True
    s1= "ab"
    s2 = "eidboaoo"           # False
    solution = Solution()
    result = solution.checkInclusion(s1, s2)
    print(result)
