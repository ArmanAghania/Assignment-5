def pascal(n):
    l=[]
    for i in range(n):
        l.append([1]*(i+1))
        
    for i in range(2,n):  
        for j in range(1,i)  :
            l[i][j]=l[i-1][j-1]+l[i-1][j]
            
    return l       
num=int(input("Enter Number: "))
a = pascal(num)
for i in a:
    print(i)