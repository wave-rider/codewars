def snail(array, result = None, level = 0):
    if result is None:
        result = []
    array_length = len(array)
    if array_length is 0: return result
    index = level
    # -->
    while index < array_length - level:
        result.append(array[level][index])
        index += 1
    # |
    # v
    index = level + 1
    while index < array_length - level:
        result.append(array[index][array_length-level-1])
        index += 1
    # <--
    index = array_length - level - 2
    while index >= level:
        result.append(array[array_length-level-1][index])
        index -= 1

    if level == array_length - 2:
        return result
    # ^
    # |
    index = level + 2
    while index > level:
        result.append(array[index][level])
        index -= 1

    return snail(array, result, level + 1)

array = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9,10,11, 12],
         [13,14,15,16]]
print(snail(array))

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array))
expected = [1,2,3,6,9,8,7,4,5]

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(array))

expected = [1,2,3,4,5,6,7,8,9]

