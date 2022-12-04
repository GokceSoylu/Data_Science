def sum(a):
    if a==0:
        return 0
    return a+sum(a-1)

a=int(input("please enter a number"))
print(sum(a))