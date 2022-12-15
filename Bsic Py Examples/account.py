class Account:
    def __init__(self,name, money):
        self.money=money
        self.name=name
    def draw(self,amount):
        if amount>0:
            self.money-=amount
    def printAccount(self):
        print(self.name,self.money)

a1=Account("necmiye",100)
a1.printAccount()
a1.draw(int(input("how many do you want to draw ")))
a1.printAccount()


# kurucu fonksiyon için _init_ yazıyoruz bu kurucu fonk demek bird her fonsiyona init de dahil self parametresi gönderilmeliself parametresi
#this anahtar kelimesi ile aynı. ancak burada self kelimesi sınıfın her özelliği için kullanılmalı çünkü başta değişkenkeri tanımlamadığımız
#için self i kullanmazsak sınıfın kendi özelliği oldupunu bşlmez :))