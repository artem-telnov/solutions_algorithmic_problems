from typing import List


class Solution:
    def solution(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                # Если target между первым и последним, 
                # значит мы нашли нужную нам строку.
                return self.binary_search(row, target)
        return False

    def binary_search(self, nums: List[int], target: int) -> bool:
        """
        Классический бинарный поиск. 
        О нем можно почитать в задаче binary_search.
        """
        left, rigth = 0, len(nums) -1

        while left <= rigth:
            mid = (left + rigth) // 2

            if target == nums[mid]:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                rigth = mid - 1

        return False