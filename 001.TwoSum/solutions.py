class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seed = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seed:
                return [seed[diff], i]
            else:
                seed[nums[i]] = i

if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}

    test_case['case1'] = [[2, 7, 11, 15], 9, [0, 1]]
    test_case['case2'] = [[3, 2, 4], 6, [1, 2]]
    test_case['case3'] = [[3, 3], 6, [0, 1]]

    for key, val in test_case.items():
        ans = sol.twoSum(nums = val[0], target = val[1])
        if ans == val[2]:
            result[key] = key + ' pass'

    print (result)