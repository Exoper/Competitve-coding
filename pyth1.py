T= int(input())
key=[]
value=[]
for i in range(T):
    k= input()
    v = input()
    key.append(k)
    value.append(v)
def sol(a):
    o=0
    w = []
    for i in range(len(a)):
        if int(a[i])==1:
            w.append(i)
    n1 = (w[0]//2)
    n2 = (len(a)-1-w[-1])//2
    
    for i in range(0,len(w)-1):
        if (w[i+1]-w[i])//2 != 1:
            o += ((w[i+1]-w[i])//2)-1
    print(n1+n2+o)
    return 0
for i in range(len(value)):
    sol(value[i])
    