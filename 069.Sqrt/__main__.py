class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid -1
            else:
                return mid
            
        return right
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}
    
    test_case['case1'] = [4, 2]
    test_case['case2'] = [8, 2]

    for key, val in test_case.items():
        ans = sol.mySqrt(val[0])
        if ans == val[1]:
            result[key] = key + ' pass'

    print (result)