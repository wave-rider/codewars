def solution(roman):
    """complete the solution by transforming the roman numeral into an integer"""
    dict = { "I" : 1, "II" : 2, "III" : 3, "V": 5,
             "X" : 10,
             'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
    order = 'IVXLCDM'

    current_token_count = 0
    current_token = ''
    total = 0;
    index = 0

    while index < len(roman):
        roman_character = roman[index]
        if current_token == roman_character or current_token == '':
            current_token = roman_character
            current_token_count += 1
        else:
            subtotal = dict[current_token] * current_token_count
            if order.index(roman_character) > order.index(current_token):
                total = total - subtotal + dict[roman_character]
                current_token_count = 0
                current_token = ''
            else:
                total = total + subtotal
                current_token = roman_character
                current_token_count = 1

        index += 1
    if current_token != '':
        total += dict[current_token] * current_token_count
    return total

result = solution("MDCLXVI")
print(result)


result = solution("I") #1
print(result)

result = solution("IX") #9
print(result)

result = solution("XXI") #21
print(result)

result = solution("CXXI")
print(result)

print ("CXXI".count("X"))

