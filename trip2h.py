N= int(input())
l1= []
l2=[]
for i in range(10**5):
    if i%2 == 0:
        l1.append(1)
        l2.append(2)
    else:
        l1.append(2)
        l2.append(1)
while(N>0):
    
            
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
    c =0
    a = 0
    if n == 1:
        print('YES')
        print(1)
        continue
    
    if k == 2:
        
        for i in range(len(arr)):
            if l1[i]==1 and arr[i] ==2:
                c = -1
                break
            if l1[i]==2 and arr[i] ==1:
                c = -1
                break
        if c == -1:
            c = 0
            a = -1
            for i in range(len(arr)):
                if l2[i] == 2 and arr[i] ==1:
                    c =-1
                    break
                if l2[i] == 1 and arr[i] == 2:
                    c = -1 
                    break
        if c == 0:
            if a == 0 and k == 2:
                print('YES')
                print((*l1[:n]))
            if a == -1 and k==2:
                print('YES')
                print(*l2[:n])
        elif k == 2:
            print('NO')

    else:
        d = 0
        l = []
        if arr[0] == -1 and arr[1] != 1:
            arr[0] = 1
        elif arr[0] == -1 and arr[1] == 1:
            arr[0] = 2
        if arr[-1] == -1 and arr[-2] != 1:
            arr[-1] = 1
        elif arr[-1] == -1 and arr[-2] == 1:
            arr[-1] = 2
        
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1] and arr[i] != -1:
                d = -1
                break
            
            elif arr[i] == -1:
                l.append(i)
    
        for i in range(len(l)):
            if arr[l[i]-1] != 1 and arr[l[i]+1]!=1:
                arr[l[i]] = 1
            elif arr[l[i]-1] != 2 and arr[l[i]+1] !=2:
                arr[l[i]] = 2
            elif arr[l[i]-1]!= 3 and arr[l[i]+1] !=3 :
                arr[l[i]] = 3
        if len(l) == 0:
            d +=0
            #if d == 0 and len(l)>0:
               #for i in range(len(l)-1):
        if d == 0:
            print('YES')
            print(*arr)
         
        if d == -1:
            print('NO')
    N-=1
