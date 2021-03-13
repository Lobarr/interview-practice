from typing import List


def totalFruit(trees: List[int]) -> int:
    treeIndexes = {}
    paths = []
    path = []
    selectedTreesPair = set([])
    for index in range(len(trees) - 1, -1, -1):
        print(index, trees[index], 'selectedPair', selectedTreesPair)

        if trees[index] in treeIndexes:
            treeIndexes[trees[index]].append(index)
        else:
            treeIndexes[trees[index]] = [index]

        if len(selectedTreesPair) < 2:
            print('adding to selected pair')
            selectedTreesPair.add(trees[index])

        if trees[index] not in selectedTreesPair:
            print('new node encountered')
            paths.append(path)
            path = [trees[index]]
            selectedTreesPair = set([trees[index]])
            nextIndex = index + 1
            if nextIndex < len(trees):
                nextIndexTree = trees[nextIndex]
                selectedTreesPair.add(nextIndexTree)
                print('backtracking')
                for i in range(nextIndex, len(trees)):
                    if trees[i] is nextIndexTree:
                        print('found index')
                        path.append(trees[i])
                    break
                print('prevNode -> selectedPair', selectedTreesPair)
        else:
            path.append(trees[index])

    if len(path) > 0:
        paths.append(path)

    maxPathCount = 0
    for path in paths:
        print(path)
        if len(path) > maxPathCount:
            maxPathCount = len(path)
    return maxPathCount
