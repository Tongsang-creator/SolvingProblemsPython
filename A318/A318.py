
init_odd = 1
init_even = 2
jump = 2
count = 0
ans = 0
end = False
n, k = input().split()
n,k = int(n),int(k)
for i in range(init_odd,n+1,jump):
    count+=1
    if(count == k):
        print(i)
        end = True
        break
#print(count)
if not end :   
    for i in range(init_even,n+1,jump):
        #print(i)
        count+=1
        if(count == k):
            print(i)
            break
