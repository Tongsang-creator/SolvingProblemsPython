init = 0

def change_type(x):
    return int(x)

def input_keyboard():
    try:
        return(input().split())
    except KeyboardInterrupt:
        print("Keyboard input error")

def subtract(n,k):
    for _ in range(init,k):
        if n%10 == 0:
            n=int(n/10)
        else:
            n -=1
    return n   

n,k = input_keyboard()
n = change_type(n)
k = change_type(k)
print(subtract(n,k))



