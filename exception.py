#yine birden fazla exception var else partı olurda hat olmazsa diye var
try:
    a=int(input())
    b=int(input())
    print(a/b)
except ZeroDivisionError:
    print("connot divide zero")
except:
    print("there is problem")
else:
    print("there was no problem")
finally:
    print("the part which always works")
