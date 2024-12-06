class Solution:
    def list_bounds(num: int) -> list:
        results = []
        for idx in range((num // 10) + (1 if num % 10 > 0 else 0)):
            _ll = idx * 10
            _uu = min((idx + 1) * 10, num)
            results.append([_ll, _uu])

        return results
