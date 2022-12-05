class LineCounter:
    def __init__(self, file_name):
        self.file=open(file_name,"r")
        self.lines=[]
    def read(self):
        self.lines=[itr for itr in self.file]
    def count(self):
        return len(self.lines)
    def get_lines(self):
        return self.lines

def read(file_name):
    file=open(file_name,"r")
    return [line for line in file]

def count(lines):
    return len(lines)

l=LineCounter("student")
l.read()
print(l.count())

try_line=read("student")
print(count(try_line))
print(count(l.get_lines()))

# burada pure olan sınıf içinde olmayan kendi başına fonksiyon olanlar. birbirlerinden etkilenmezler normal fonksiyanel programlama mantığı
#class içerisidekş metodlar ise unpure. yan etkileri vardır. sadece bir parametre vrir ve sadece çıkış alamyı beklersin ama başka etkşleri de olur
#metodlar birbirlerini ve varaible ları etkiler