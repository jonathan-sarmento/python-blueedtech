# from math import factorial
# import random

# result = list()

# cont = 0
# # while cont < 10**6:
# #     string = f'{random.randint(1, 10)} - {random.randint(11, 20)} - {random.randint(21, 30)} - {random.randint(31, 40)} - {random.randint(41, 50)} - {random.randint(51, 60)}'

# #     if not(string in result):
# #         result.append(string)
# #         # print(result[cont])
# #         cont += 1

# print(factorial(60)/(factorial(6)*factorial(60-6)))
import itertools
lista = list(range(1, 61))

for x in itertools.combinations(lista, 6):
    print(x)
