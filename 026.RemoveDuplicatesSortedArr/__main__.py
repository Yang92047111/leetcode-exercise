class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
    
if __name__ == '__main__':
    def validLength(nums, ans, expected):
        assert(ans == len(expected))
        for i in range(ans):
            assert( nums[i] == expected[i])

    sol = Solution()

    test_case = {}
    result = {}

    test_case['case1'] = [[1, 1, 2], 2, [1, 2]]
    test_case['case2'] = [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]]

    for key, val in test_case.items():
        ans = sol.removeDuplicates(val[0])
        validLength(val[0], ans, val[2])
        if ans == val[1]:
            result[key] = key + ' pass'

    print (result)