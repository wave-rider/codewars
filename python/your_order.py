import re
import collections
def order(sentence):
  a = sentence.split()
  b = re.findall(r'\d+', sentence)

  index = 0
  dict = {}

  while index < len(b):
      dict[b[index]] = a[index]
      index += 1

  ordered_dict = collections.OrderedDict(sorted(dict.items()))

  return " ".join(ordered_dict.values())

x = order("is2 Thi1s T4est 3a")
print(x)
