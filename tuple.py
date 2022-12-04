#tupe aynı liste gibidir ancak () ile tanımlanır ve değiştirilemez :)
#yine sıralıdır ve çeşitli değişkenler tiplerini birden barındırabilir
t=('a',2,3,4,'e')
print(t[0])

t1=('x','y','z',1,2,3,[4,5,6])

print(t1[6])
print(t1[6][0])
#nasıl şok oldun dimi :))

#tuple initilize etnmek için birden fazla yöntem ver. yukarıdaki gibi () yapılabilir parantezsiz yapilabşlir. asdece tek elemanlıysa sona, konmalı
t2=12,'s','d'
t3=15,
t4=()
t5=tuple()

# mine indis te kullanabiliriz bu tuple a has bir özellik değil bunu listed e yapabilriz -1 son eleman olmak üzere sondan bir onceki -2 olur
#yine for gibi yazdırırdık ya[::] bu tuple da da geçerli
print(t[-3])
print(t[-5:-2:1]) 
print(t[-1:-5:-1]) 