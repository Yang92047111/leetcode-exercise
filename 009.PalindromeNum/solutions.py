class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        rev_x = x[::-1]
        if x == rev_x:
            return True

        return False
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}

    test_case['case1'] = [121, True]
    test_case['case2'] = [-121, False]
    test_case['case3'] = [10, False]

    for key, val in test_case.items():
        ans = sol.isPalindrome(val[0])
        if ans == val[1]:
            result[key] = key + ' pass'

    print (result)