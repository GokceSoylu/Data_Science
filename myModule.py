def power(n):
    return lambda a: a**n
def increase(n):
    return lambda a: a+10 if n%2==0  else a+1
ten=increase(2)
one=increase(3)
square=power(2)
treeple=power(3)