class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1

        return i, nums
    
if __name__ == '__main__':
    def validLength(nums, ans, expected):    
        assert(ans == len(expected))
        for i in range(ans):
            assert(nums[i] == expected[i])

    sol = Solution()

    test_case = {}
    result = {}

    test_case['case1'] = [[3, 2, 2, 3], 3, 2, [2, 2]]
    test_case['case2'] = [[0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]]

    for key, val in test_case.items():
        ans, res = sol.removeElement(val[0], val[1])
        validLength(res, ans, val[3])
        if ans == val[2]:
            result[key] = key + ' pass'

    print (result)