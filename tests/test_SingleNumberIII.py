from leetcode.SingleNumberIII import Solution


class TestSolution:
    def test_singleNumber1(self):
        nums = [1, 2, 1, 3, 2, 5]
        s = Solution()
        result = s.singleNumber(nums)
        assert result == [3, 5] or result == [5, 3]

    def test_singleNumber2(self):
        nums = [-1, 0]
        s = Solution()
        result = s.singleNumber(nums)
        assert result == [-1, 0] or result == [0, -1]

    def test_singleNumber3(self):
        nums = [0, 1]
        s = Solution()
        result = s.singleNumber(nums)
        assert result == [0, 1] or result == [1, 0]

    def test_singleNumber4(self):
        nums = [1, 1, 3, 3, 5, 6]
        s = Solution()
        result = s.singleNumber(nums)
        assert result == [5, 6] or result == [6, 5]

    def test_singleNumber5(self):
        nums = [-283, -174, 44, -174, 40, 40, 101, 101, 354, -283, 513, 513]
        s = Solution()
        result = s.singleNumber(nums)
        assert result == [44, 354] or result == [354, 44]
