class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}
    
    test_case['case1'] = ["11", "1", "100"]
    test_case['case2'] = ["1010", "1011", "10101"]

    for key, val in test_case.items():
        ans = sol.addBinary(val[0], val[1])
        if ans == val[2]:
            result[key] = key + ' pass'

    print (result)