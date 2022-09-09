import random as r
import matplotlib.pyplot as m
i=1
n=0
j=[]
g=[]
m.axis([1,1000,1,6])
while i<=1000:
    n=r.randint(1,6)+n
    d=n/i
    j.append(i)
    g.append(d)
    m.plot(j,g)
    i+=1
m.show()