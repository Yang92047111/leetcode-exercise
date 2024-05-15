class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sp = s.split()
        i = len(sp[-1])
        return i
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}
    
    test_case['case1'] = ["Hello World", 5]
    test_case['case2'] = ["   fly me   to   the moon  ", 4]
    test_case['case2'] = ["luffy is still joyboy", 6]

    for key, val in test_case.items():
        ans = sol.lengthOfLastWord(val[0])
        if ans == val[1]:
            result[key] = key + ' pass'

    print (result)