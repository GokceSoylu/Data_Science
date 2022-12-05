def power(n):
    return lambda a: a**n

squre=power(2)
treeple=power(3)

print(squre(3))
print(treeple(3))


#print(power(2)) bu olmaz ama