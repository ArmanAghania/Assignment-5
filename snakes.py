def snake(n,m):
    for ii in range (m):
        for i in range(3,n + 3):
            if ii%2 == 1:
                if i%2 == 1:
                    print('*', end = '')
                else:
                    print('#', end = '')
            else:
                if i%2 == 1:
                    print('#', end = '')
                else:
                    print('*', end = '')
        print('/n')   
    return
n = int(input('How long do you want your snake to be?! '))
m = int(input('How many snakes do you want?! '))

snake(n,m)

