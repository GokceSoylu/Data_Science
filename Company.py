class Costumer_access:
    __Company="Simurg"# __ işareti private yapmaktır ancak hocam __init__ private değil o başka. private özellikleri java ile aynı. sadece sınıf içerisinde kullanılabilirr
    def __init__(self,pasword,name):
        self.name=name
        self.pasword=pasword
    def printCompany(self):
        a=int(input("pasword... "))
        if a==self.pasword:
            print(Costumer_access.__Company)#static 
        else:
            print("wrong pasword")
class Employee_access(Costumer_access):
    def __init__(self,pasword,name):
        super().__init__(pasword,name)

class Manangmant_access(Employee_access):
    __money=0
    def __init__(self,posword,name):
        super().__init__(posword,name)
    def addMoney(self,amount):
        Manangmant_access.__money+=amount
    def drawMoney(self,amount):#!           yahu self'i kullanmıyıcam da desen parametre olarak yazılmak zorunda 
        Manangmant_access.__money-=amount
    def printMonay(self):
        print(Manangmant_access.__money)

cos= Costumer_access(int(input("pasword ")),input("name "))
em=Employee_access(int(input("pasword ")),input("name "))
man=Manangmant_access(int(input("pasword ")),input("name "))

cos.printCompany()
man.addMoney(int(input("money ")))
man.drawMoney(int(input("money ")))
man.printMonay()
man.printCompany()