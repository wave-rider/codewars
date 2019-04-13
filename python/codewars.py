import unittest
def delete_nth(order,max_e):
    dict = {}
    result = []
    for item in order:
        if item in dict:
            if dict[item] < max_e:
                dict[item] = dict[item] + 1
                result.append(item)
        else:
                dict[item] = 1
                result.append(item)
    return result
    # code here

a = delete_nth([20,37,20,21], 1) # [20,37,21])
print(a)
a = delete_nth([1,1,3,3,7,2,2,2,2], 3) #, [1, 1, 3, 3, 7, 2, 2, 2])
print(a)
