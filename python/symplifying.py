def parse_expression(expression):
    result = {}
    index = 0
    stack = []
    for item in expression:
        if item == '-':
            stack.append(item)
            continue
        if item == '+':
            stack.append(item)
            continue
        if item == ' ':
            continue
        if item.isnumeric():
            if len(stack) > 0 and stack[-1].isnumeric():
                stack[-1] += item
            else:
                stack.append(item)
        else:
            if item in result:
                if len(stack) > 0 and type(stack[-1]) is int:
                    from_stack = stack.pop()


def simplify(examples,formula):
    return formula[0]



examples=[["a + a = b", "b - d = c", "a + b = d"],
          ["a + 3g = k", "-70a = g"],
          ["-j -j -j + j = b"]
         ]
formula=["c + a + b",
         "-k + a",
         "-j - b"
        ]
answer=["2a",
        "210a",
        "1j"
        ]

result = simplify()

