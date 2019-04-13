def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    array3 = [x**2 for x in array1]
    array3.sort()
    array2.sort()
    return array2 == array3

a1 = [122, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
print(comp(a1, a2))
