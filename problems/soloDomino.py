def soloDomino(A: list, B: list, K: int):
    selectedLevel = A if sum(A) > sum(B) else B
    selectedFirst = selectedLevel == A
    diff = []

    for index in range(len(selectedLevel)):
        if selectedLevel == A:
            diff.append(B[index] - A[index])
        else:
            diff.append(A[index] - B[index])

    while K > 0:
        maxIndex = 0
        for index in range(1, len(diff)):
            if diff[index] > diff[maxIndex]:
                maxIndex = index
        if selectedFirst:
            selectedLevel[maxIndex] = A[maxIndex]
        else:
            selectedLevel[maxIndex] = B[maxIndex]
        K -= 1

    return sum(selectedLevel)
