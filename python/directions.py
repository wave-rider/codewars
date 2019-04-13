def dirReduc(arr):
    result = []
    index = len(arr) - 1
    while index > 0:
        if arr[index] == arr[0]:
            return result
        result.insert(0, arr[index])
        index -= 1
        if index==0:
            result.insert(0, arr[index])


    return result


u=["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u))
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a))#, ['WEST'])
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH"])) #// => @[]

