from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    """Given sorted array, return 2 not zero-based indices that sum to target.

    index 1 must be less than index2."""

    # *** 2-pointer ***
    
    # indices are not zero-based ( therefor + 1 to each index )
    
    start = 0
    end = len(numbers) - 1
    
    while start < end:
        if numbers[start] + numbers[end] == target:
            return start + 1, end + 1
        if numbers[start] + numbers[end] < target:
            start += 1
        if numbers[start] + numbers[end] > target:
            end -= 1


if __name__ == '__main__':
    
    print(twoSum([2,7,11,15], 9))  # 1, 2
    print(twoSum([2,3,4], 6))  # 1,3