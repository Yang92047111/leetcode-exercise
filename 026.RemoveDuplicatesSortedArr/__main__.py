class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}

    test_case['case1'] = [[1, 1, 2], 2]
    test_case['case2'] = [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5]

    for key, val in test_case.items():
        ans = sol.removeDuplicates(val[0])
        if ans == val[1]:
            result[key] = key + ' pass'

    print (result)