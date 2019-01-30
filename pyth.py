T = int(input())
R , C , K =[],[],[]
for i in range(T):
    r,c,k = map(int,input().split())
    R.append(r)
    C.append(c)
    K.append(k)

def sol(a,b,d):
    l,m=[],[]
    l.append(a)
    m.append(b)
    i=1
    while(d>0):
        l.append(a+i)
        l.append(a-i)
        m.append(b+i)
        m.append(b-i)
        i+=1
        d-=1
    m1 = [x for x in m if x<=8 and x>0]
    l1 = [x for x in l if x<=8 and x>0]


    r1 = max(l1)
    r2 = min(l1)
    c1 = max(m1)
    c2 = min(m1)
    print((r1-r2+1)*(c1-c2+1))
    return 0

for i in range(T):
    sol(R[i],C[i],K[i])
