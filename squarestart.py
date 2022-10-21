n=int(input("enter any number:"))
for i in range(n):
    print(" "*(n-1-i)+("* ")*(i+1))
for i in range(n):
    print(" "*(i+1)+("* ")*(n-1-i))

"""n=int(input("enter any number:"))
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1 or j==0 or j==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""
    

"""side = int(input("Please Enter any Side of a Square  : "))
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side-1 or j == 0 or j == side-1):
            print('*', end = ' ')
        else:
            print(' ', end = ' ')
    print()"""

