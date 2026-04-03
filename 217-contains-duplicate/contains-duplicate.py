class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        siri = set()
        for num in nums:
            if num in siri:
                return True
            siri.add(num)
        return False