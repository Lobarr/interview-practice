from collections import Counter


def twoSum(nums, target):
    check = Counter(nums)

    for num in nums:
        complement = target - num

        if complement in check:
            if complement == num:
                if check[complement] >= 2:
                    return True
                return False

            return True

    return False


if __name__ == '__main__':
    test_cases = [
        # (nums, target, expected)
        ([4, 2, 6, 5, 7, 9, 10], 13, True)
    ]

    for test_case in test_cases:
        assert twoSum(test_case[0], test_case[1]) == test_case[2]

    print('Test Passed')
