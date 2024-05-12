class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}

    test_case['case1'] = ["()", True]
    test_case['case2'] = ["()[]{}", True]
    test_case['case3'] = ["(]", False]

    for key, val in test_case.items():
        ans = sol.isValid(val[0])
        if ans == val[1]:
            result[key] = key + ' pass'

    print (result)