T = int(input())
N,A,B,K = [],[],[],[]
for i in range(T):
    n,a,b,k = map(int,input().split())
    N.append(n)
    A.append(a)
    B.append(b)
    K.append(k)
def sol(ni,ai,bi,ki):
    a1 = ni//ai
    a2 = ni//bi
    c=0
    def lcm(x, y):  
        if x > y:
            greater = x  
        else:  
            greater = y  
        while(True):  
            if((greater % x == 0) and (greater % y == 0)):  
                lcm = greater  
                break  
            greater += 1  
        return lcm
    c = ni//lcm(ai,bi)
    f = a1+a2-(2*c)
    if f>=ki:
        print("Win")
    else:
        print("Lose")
for i in range(T):
    sol(N[i],A[i],B[i],K[i])