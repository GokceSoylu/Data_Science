import numpy as np
a=np.arange(10,100,10)
print(a[:])
print(a.shape)
a=np.reshape(a,(3,3))
# a=a.reshape((3,3)) üstteki de uda çalışır sorun yok :))
print(a.shape)

ar=[1,2,3],[4,5,6]
ar=np.reshape(ar,-1) # mesela burada arr.reshape() şeklinde çalıştıröıyoruz bu gibi dır-rumlar için np.reshappe şeklinde çalıştırmak gerekli
print(ar[:])

