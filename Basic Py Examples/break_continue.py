#break continue  c ile aynı bunlar hiç bir dil de değişmiyor :)
i=-1
while i<10:
    i+=1
    if i==10 or i==0:
            continue
    #i+=1 hocam continue alttaki kodları bırak döngünün başına dön demek ya işte direkt
    #döngünün başına gittiği için i artmıyor ve sonzsuz döngü oluyor. ancak bu python a has
    #bir sıkıntı değil bu arttımayı c de de continue dan sonra ya koyasan ora da aynı sıkıntı olur
    print(i)