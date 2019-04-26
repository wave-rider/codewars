def kebabize(s):
    result = ""

    for c in s:
        if c.isalpha():
            if c.isupper():
                if len(result) > 0:
                    result += '-'
            result += c.lower()

    return result


x = kebabize('myCamelCasedString')
print(x)
