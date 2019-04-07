def is_stupid_pair(a, b):
    pair = [a,b]
    pair.sort()
    stupid_pair = False
    if (pair[0] == 'NORTH' and pair[1] == 'SOUTH') or (pair[0] == 'EAST' and pair[1] == 'WEST'):
            stupid_pair = True
    return stupid_pair

def dirReduc(arr):
    if len(arr) < 2:
        return []
    index = 1
    result = arr[:]
    while index < len(result):
        stupid_pair = is_stupid_pair(result[index], result[index-1])
        if stupid_pair:
            start_part = result[:index-1]
            end_part = result[index+1:]
            result = start_part + end_part
            index = 1
        else:
            index += 1

    if len(result) > 2 and result[0]==result[-1]:
        return []
    return result

g = ['NORTH', 'NORTH', 'NORTH', 'NORTH', 'SOUTH', 'SOUTH', 'SOUTH', 'SOUTH']
print(dirReduc(g))# []
g = ['WEST', 'SOUTH', 'EAST', 'NORTH', 'EAST', 'SOUTH', 'SOUTH', 'WEST']
print(dirReduc(g))# []
g = ['SOUTH', 'EAST', 'SOUTH', 'WEST', 'WEST', 'SOUTH']
print(dirReduc(g))# []
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))# ['WEST']
u=["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u))# ["NORTH", "WEST", "SOUTH", "EAST"])
g = ["NORTH", "SOUTH", "EAST", "WEST"]
print(dirReduc(g))# []
g = ["NORTH", "SOUTH", "EAST", "WEST", "WEST"]
print(dirReduc(g))# ['WEST']
g = ["NORTH", "SOUTH", "EAST", "WEST", "WEST", "SOUTH", "EAST"]
print(dirReduc(g))# ['WEST', 'SOUTH', 'EAST']
g = ["NORTH", "SOUTH", "EAST", "WEST", "SOUTH", "EAST"]
print(dirReduc(g))# ["SOUTH", "EAST"]
g = ["NORTH"]
print(dirReduc(g))# []



