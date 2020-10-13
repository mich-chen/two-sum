from typing import List

class Solution:

    """
    # ***** Hashmap solution *****

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indices = {}
        for i, value in enumerate(nums):
            remaining = target - value
            if remaining in indices:
                return [indices[remaining], i]
            indices[value] = i
        return []
    """

    # ***** 2-pointer solution *****
    # must return indices from the original nums array
        
    # tuples of (index, element), sorted by element
    # as if we have sorted list of nums, but need to still keep track of original index
        # turn enumerate object to list --> elements are (index, num)
        # key for sorted() will sort by the num element
    nums_sorted = sorted(list(enumerate(nums)), key=lambda x: x[1])
    # initialize pointers to beginning and end of array
    start = 0
    end = len(nums) - 1
    
    # looking at two numbers, so can ignore the last index
    while start < end:
        # index into element, if sums == target, return the original index
        sums = nums_sorted[start][1] + nums_sorted[end][1]
        if sums == target:
            return nums_sorted[start][0], nums_sorted[end][0]
        # move pointers if sum is not target
        if sums < target:
            start += 1
        if sums > target:
            end -= 1


if __name__ == '__main__':

    testcase = Solution()
    print(testcase.twoSum([2, 7, 11, 15], 9))
    print(testcase.twoSum([3, 2, 4], 6))
    print(testcase.twoSum([3, 3], 6))
