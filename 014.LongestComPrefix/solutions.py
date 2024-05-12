class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        s = ""

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return s

            s += strs[0][i]
        
        return s
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}

    test_case['case1'] = [["flower","flow","flight"], "fl"]
    test_case['case2'] = [["dog","racecar","car"], ""]

    for key, val in test_case.items():
        ans = sol.longestCommonPrefix(val[0])
        if ans == val[1]:
            result[key] = key + ' pass'

    print (result)