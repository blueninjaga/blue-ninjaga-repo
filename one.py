# print(85 % 9)
# a = 3
# b = 4
# print(a+b)
# def function(one,two):
#     c = one + two
#     return c
#
# print(function(5,10))
# print(10>9)

# x = 0
# x += 3
# x -= 3
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# for elem1 in a:
#
#     for elem2 in b:
#         if elem1 == elem2:
#             c.append(elem1)
# print(c)
d = {"меркурий": 1, "земля": 3, "марс": 4, "венера": 2, "солнце": 0}


result = sorted(d, key=d.get, reverse=False)
print(result)