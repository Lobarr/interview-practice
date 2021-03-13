def urlify(url: str, trueLen: int):
    spaceIndexes = []
    charsCount = 0
    for index, char in enumerate(url):
        if char == " ":
            spaceIndexes.append(index)
        else:
            charsCount += 1

    # remove unessacry spaces from the back
    allowedNumSpaces = trueLen - charsCount
    while len(spaceIndexes) > allowedNumSpaces:
        spaceIndex = spaceIndexes.pop()
        url = url[0:spaceIndex] + url[spaceIndex + 1:]

    offset = False
    for allowedSpaceIndex in spaceIndexes:
        if offset:
            allowedSpaceIndexOffset = allowedSpaceIndex + (3 - 1)
            url = url[0:allowedSpaceIndexOffset] + "%20" + url[
                allowedSpaceIndexOffset + 1:]
        else:
            url = url[0:allowedSpaceIndex] + "%20" + url[allowedSpaceIndex +
                                                         1:]
            offset = True
    return url
