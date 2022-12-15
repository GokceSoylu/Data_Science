c=10
def power(a,b):
    print("a^b =",str(a**b))
    return a**b
def product(a):
    return a*c
power(4,3)
print(product(power(2,3)))

#global değişken kullandık. önce locali taradi bulamyınca global değişkeni kullandı
#?birde dikkatimi çekti return olan fonksiyonalrı bir yere atamasakta sıkıntı yapmıyor 