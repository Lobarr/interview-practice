def isUniqueMap(string):
    check = {}
    for char in string:
        if char in check:
            return False
        check[char] = True
    return True


def isUniqueAscii(string):
    ASCII_LEN = 128
    ascii_map = [False for _ in range(ASCII_LEN)]

    if len(string) > ASCII_LEN:
        return False

    for char in string:
        if ascii_map[char]:
            return False
        ascii_map[char] = True

    return True
