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

    case1 = [[2, 7, 11, 15], 9, [0, 1]]
    case2 = [[3, 2, 4], 6, [1, 2]]
    case3 = [[3, 3], 6, [0, 1]]

    result1 = sol.twoSum(nums = case1[0], target = case1[1])
    result2 = sol.twoSum(nums = case2[0], target = case2[1])
    result3 = sol.twoSum(nums = case3[0], target = case3[1])

    if result1 == case1[2]:
        print('Case1 pass')
    else:
        print('Case1 false')

    if result2 == case2[2]:
        print('Case2 pass')
    else:
        print('Case2 false')

    if result3 == case3[2]:
        print('Case3 pass')
    else:
        print('Case3 false')