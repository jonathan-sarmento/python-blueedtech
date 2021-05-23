def contador(i, f, p):
    if i < f:
        for x in range(i, f+1, p):
            print(x)
    else:
        for x in range(i, f-1, -1*p):
            print(x)


contador(1, 10, 1)
print('-'*15)
contador(10, 0, 2)
print('-'*15)
contador(0, 20, 5)
