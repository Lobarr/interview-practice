def getBit(bits, index):
    return (bits & (1 << index)) != 0


def setBit(bits, index):
    return bits | (1 << index)


def clearBit(bits, index):
    return bits & ~(1 << index)


def clearFromLeftToIndex(bits, index):
    mask = (1 << index) - 1
    return bits & mask


def clearBits(bits, index):
    mask = -1 << (index + 1)
    return bits & mask


def updateBit(bits, index, newBit):
    assert newBit == 1 or newBit == 0
    return clearBit(bits, index) | (newBit << index)


# Problems


def insertion(N, M, i, j):
    modifiedBits = N
    modifierBitsIndex = 0
    for k in range(i, j):
        newBit = getBit(M, modifierBitsIndex)
        modifiedBits = updateBit(N, k, newBit)
        modifierBitsIndex += 1
    return modifiedBits
