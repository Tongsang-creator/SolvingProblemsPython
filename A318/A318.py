
init_odd = 1
init_even = 2
jump = 2
count = 0
ans = 0
end = False
n, k = input().split()
n,k = int(n),int(k)

if(n%2 != 0):
    if( k <= int(n/2)+1):
        print(k*2-1)
    else:
        print((k-int(n/2)-1)*2)
else:
    if( k <= int(n/2)):   
        print(k*2-1)
    else:
        print((k-int(n/2))*2)