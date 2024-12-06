class Solution:
    def list_bounds(num: int) -> list:
        results = []
        for _ll in range(0, num, 10):
            _uu = min(_ll + 10, num)
            results.append([_ll, _uu])

        return results
