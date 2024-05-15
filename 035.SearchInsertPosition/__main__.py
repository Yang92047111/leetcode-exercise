class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
            
        return len(nums)
    
if __name__ == '__main__':
    sol = Solution()

    test_case = {}
    result = {}
    
    test_case['case1'] = [[1, 3, 5, 6], 5, 2]
    test_case['case2'] = [[1, 3, 5, 6], 2, 1]
    test_case['case2'] = [[1, 3, 5, 6], 7, 4]

    for key, val in test_case.items():
        ans = sol.searchInsert(val[0], val[1])
        if ans == val[2]:
            result[key] = key + ' pass'

    print (result)