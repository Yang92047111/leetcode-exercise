class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prev2 = 0
        for i in range(1, n + 1):
            curi = prev + prev2
            prev2 = prev
            prev = curi

        return prev
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}
    
    test_case['case1'] = [2, 2]
    test_case['case2'] = [3, 3]

    for key, val in test_case.items():
        ans = sol.climbStairs(val[0])
        if ans == val[1]:
            result[key] = key + ' pass'

    print (result)