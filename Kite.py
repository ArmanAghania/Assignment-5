def diamond(n):
    for ii in range(n):
        print(' '*(n-ii), '*'*(2*ii + 1))
    for ii in range(n-2, -1, -1):
        print(' '*(n-ii), '*'*(2*ii + 1))

n = int(input('How long do you want your diamond to be?!  '))
diamond(n)