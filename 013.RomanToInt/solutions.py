class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s) - 1):
            if m[s[i]] < m[s[i + 1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans + m[s[-1]]
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}

    test_case['case1'] = ['III', 3]
    test_case['case2'] = ['LVIII', 58]
    test_case['case3'] = ['MCMXCIV', 1994]

    for key, val in test_case.items():
        ans = sol.romanToInt(val[0])
        if ans == val[1]:
            result[key] = key + ' pass'

    print (result)