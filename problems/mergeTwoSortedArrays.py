def mergeTwoSortedArrays(arr1, arr2):
    new_arr = [0] * (len(arr1) + len(arr2))
    cur_arr_index = 0
    arr1_pointer, arr2_pointer = 0, 0

    while (arr1_pointer < len(arr1) and arr2_pointer < len(arr2)):
        if arr1[arr1_pointer] < arr2[arr2_pointer]:
            new_arr[cur_arr_index] = arr1[arr1_pointer]
            arr1_pointer += 1
        elif arr1[arr1_pointer] > arr2[arr2_pointer]:
            new_arr[cur_arr_index] = arr2[arr2_pointer]
            arr2_pointer += 1
        else:
            new_arr[cur_arr_index] = arr1[arr1_pointer]
            arr1_pointer += 1

        cur_arr_index += 1

    #! add the rest incase lengths are different
    if arr1_pointer < len(arr1):
        while cur_arr_index < len(new_arr):
            new_arr[cur_arr_index] = arr1[arr1_pointer]
            arr1_pointer += 1
            cur_arr_index += 1

    if arr2_pointer < len(arr2):
        while cur_arr_index < len(new_arr):
            new_arr[cur_arr_index] = arr2[arr2_pointer]
            arr2_pointer += 1
            cur_arr_index += 1

    return new_arr


if __name__ == "__main__":
    test_cases = [
        # (input_arr1, input_arr2, expected)
        ([1, 3, 5], [2, 4, 6, 8, 10], [1, 2, 3, 4, 5, 6, 8, 10]),
        ([1, 4, 8], [1, 2, 6], [1, 1, 2, 4, 6, 8])
    ]

    for test_case in test_cases:
        assert mergeTwoSortedArrays(test_case[0], test_case[1]) == test_case[2]

    print('Test Passed')
