class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}
    
    test_case['case1'] = ["sadbutsad", "sad", 0]
    test_case['case2'] = ["leetcode", "leeto", -1]

    for key, val in test_case.items():
        ans = sol.strStr(val[0], val[1])
        if ans == val[2]:
            result[key] = key + ' pass'

    print (result)