class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
                
        return [1] + digits
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}
    
    test_case['case1'] = [[1, 2, 3], [1, 2, 4]]
    test_case['case2'] = [[4, 3, 2, 1], [4, 3, 2, 2]]
    test_case['case2'] = [[9], [1, 0]]

    for key, val in test_case.items():
        ans = sol.plusOne(val[0])
        if ans == val[1]:
            result[key] = key + ' pass'

    print (result)