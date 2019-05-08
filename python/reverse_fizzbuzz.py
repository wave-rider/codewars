'''
FizzBuzz is often one of the first programming puzzles people learn. Now undo it with reverse FizzBuzz!

Write a function that accepts a string, which will always be a valid section of FizzBuzz.
Your function must return an array that contains the numbers in order that generate that section of FizzBuzz.

For instance:

reverse_fizzbuzz("1 2 Fizz 4 Buzz")   #returns [1, 2, 3, 4, 5]
reverse_fizzbuzz("Fizz 688 689 FizzBuzz") #returns [687, 688, 689, 690]
reverse_fizzbuzz("Fizz Buzz")         #returns [9, 10]
Notes:

If a sequence can appear multiple times within FizzBuzz, return the numbers that generate the first instance of that sequence.
You will never be passed an empty sequence.
All numbers in the sequence will be greater than zero.
'''
def reverse_fizzbuzz(string):
    my_list = string.split(' ')
    for index, item in enumerate(my_list):
        if item.isnumeric():
            numeric_value = int(item)
            first_value = numeric_value - index
            return list(range(first_value, first_value + len(my_list)))
    if len(my_list)==2:
        if my_list[0] == 'Fizz':
            return [9, 10]
        if my_list[0] == 'Buzz':
            return [5, 6]
    if my_list[0] == 'Buzz' and len(my_list)==1:
        return [5]
    if my_list[0] == 'Fizz' and len(my_list)==1:
        return [3]
    if my_list[0] == 'FizzBuzz' and len(my_list)==1:
        return [15]

a = reverse_fizzbuzz("1 2 Fizz 4 Buzz")
print(a)
a = reverse_fizzbuzz("Fizz 688 689 FizzBuzz")
print(a)
a = reverse_fizzbuzz("Fizz Buzz")
print(a)

