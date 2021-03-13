def sortBitArray(arr):
    left_pointer, right_pointer = 0, len(arr) - 1
    while left_pointer < right_pointer:

        while arr[left_pointer] == 0:
            left_pointer += 1

        while arr[right_pointer] == 1:
            right_pointer -= 1

        if left_pointer < right_pointer:
            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[
                left_pointer]

    return arr


test_cases = [
    # (input, expected)
    ([0, 1, 0, 1], [0, 0, 1, 1]),
    ([1, 1, 1, 0, 0], [0, 0, 1, 1, 1])
]

if __name__ == '__main__':
    for test_case in test_cases:
        assert sortBitArray(test_case[0]) == test_case[1]

    print('Test Passed')
