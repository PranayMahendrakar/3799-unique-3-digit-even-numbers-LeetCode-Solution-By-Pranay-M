class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from itertools import permutations
        result = set()
        for perm in permutations(digits, 3):
            if perm[0] != 0 and perm[2] % 2 == 0:  # no leading zero, last digit even
                num = perm[0] * 100 + perm[1] * 10 + perm[2]
                result.add(num)
        return len(result)