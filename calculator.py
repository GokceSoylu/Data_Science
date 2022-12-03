key=True
while key:
    a=int(input("please enter a number "))
    b=int(input("another number "))
    process=str(input("what is the process "))#string i bile kısaltmışlar ya 😅
    if process=='+':
        print(a,process,b,"=",(a+b))
        k=int(input("to countunio please press nine"))
        if not k==9:
            key=False
    elif process=='-':
        print(a,process,b,"=",(a-b))
        k=int(input("to contunio please press 9"))
        if k!=9:
            key=False
#özetle else if falan paranteze gerek yok hangi sırada olduklarına bakılır. condition
#kısımları için paranteze gerek yok ancak şart kısmının bittiğini belirtmek için : ifadeisni
#kullanmalıyız. != çalışıyor ama ayrıca not direkt bunu da kullanabilirsin. 
# & için and
# || için or kullanılır
#tıpkı if else gibi while da da parantez yok şart ifadesinden sonra : var