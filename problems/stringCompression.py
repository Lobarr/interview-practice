from collections import Counter

def stringCompression(string):
  compressed = []
  curChar = ''
  curCharCount = 0

  for char in string:
    if char != curChar:
      if curChar and curCharCount:
        compressed.append(curChar)
        compressed.append(str(curCharCount))
      curChar = char
      curCharCount = 1
    else:
      curCharCount += 1

  compressed.append(curChar)
  compressed.append(str(curCharCount))

  return min(string, ''.join(compressed), key=len)

def testStringCompression():
  testCases = [
    ('aabcccccaaa', 'a2b1c5a3'),
    ('abcdef', 'abcdef')
  ]
  for [testCase, expectedValue] in testCases:
    actual = stringCompression(testCase)
    print(actual, expectedValue)
    assert actual == expectedValue
