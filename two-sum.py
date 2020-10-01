from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {}
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in indices:
                return [indices[remaining], i]
            indices[value] = i
        return []


if __name__ == '__main__':

    testcase = Solution()
    print(testcase.twoSum([2, 7, 11, 15], 9))
    print(testcase.twoSum([3, 2, 4], 6))
    print(testcase.twoSum([3, 3], 6))
