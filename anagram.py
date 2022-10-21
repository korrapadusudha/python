#==========anagram==========#
"""a=(input("enput:"))
b=(input("enput:"))
if sorted(a)==sorted(b):
    print("anagram")
else:
    print("not anagram")

"""
#========unique value=======#
"""
a="zzz"
p=""
for char in a:
    if char not in p:
        p=p+char
print(p)
print(len(p))"""


#=========regx functions=======#
"""import re
str=input("enter any string:")
x=re.search("a",str)
print(x)
"""
#==========files==============#
"""myfile=open("C:/Users/Dell/OneDrive/Desktop/python.txt",'r+')
myfile.seek(8)
myfile.write("hello")
myfile.close
"""
#==========fact using functions========#
"""def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
fact(5)
"""
#=========ramdomLottery using functions======#
"""
def randomlottery(num):
    s=[]
    for i in range(num):
        n=int(input("enter any number:"))
        if n!=0:
            if n not in s:
                s.append(n)
                print(s)
            else:
                n=int(input("enter any number:"))
                s.append(n)
    print(s.sort())            
    print(s)
randomlottery(6)"""

#=========sorted order using functions=======#
"""def sorting(list):
    list1=sorted(list)
    if list==list1:
        print("true")
    else:
        print("false")
sorting([1,3,4,5,69])"""
#======converting tuple to list======#
"""tuple=(1,2,3,45)
lst=list(tuple)
print(type(lst))"""

#=========list methods======#
list1=[1,2,3,"sudha","rani",2]
print(len(list1))
print(list(list1))
list1.append([30])
print(list1)
list1.insert(2,34)
print(list1.count(2))
print(list1.index(2))
list1.remove(2)
print(list1)
list1.pop(3)
print(list1)
list1.reverse()
print(list1)

print(len,sort,sorted,min,max,sum,count,remove,reverse,list,append,insert,pop,extend,index)
print(len,title,lower,upper,count,find,index,endswith,startswith,isalnum,isupper,islower,istitle,lstrip,rstrip,strip,join,split,replace)

