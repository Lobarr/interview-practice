def sortedTwoSum(arr, target):
    left_pointer, right_pointer = 0, len(arr) - 1

    while left_pointer < right_pointer:
        temp_sum = arr[left_pointer] + arr[right_pointer]
        if temp_sum < target:
            left_pointer += 1
        elif temp_sum > target:
            right_pointer -= 1
        else:
            return True

    return False


if __name__ == '__main__':
    test_cases = [
        # (input_arr, target, expexted)
        ([2, 4, 5, 6, 7], 8, True),
        ([2, 4, 6, 7, 8, 9, 10], 15, True),
        ([2, 3, 4], 8, False)
    ]

    for test_case in test_cases:
        assert sortedTwoSum(test_case[0], test_case[1]) == test_case[2]

    print('Test Passed')
