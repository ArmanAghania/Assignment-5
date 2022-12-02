
def nest(list,rows,columns):
    rr = []
    ss = 0
    ee = columns
    for i in range(rows):
        rr.append(list[ss:ee])
        ss += columns
        ee += columns
    return rr

def mt(n,m):
    a = []
    x = 0
    for ii in range(1 , n + 1):
        for jj in range(1 , m + 1):
            a.append(ii*jj)
    l = nest(a,n,m)
    for kk in range(n):
        print(l[kk])
    

n = int(input('rows?!  '))
m = int(input('columns?!  '))

mt(n,m)