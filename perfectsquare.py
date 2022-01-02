def Num(n):
    if n<3:
        return n

    a = n

    for i in range(1, n+1):
        sq_num = i*i

        if sq_num < n:
            a = min(a, 1 + Num(n-sq_num))

        else:
            break
        
    return a

print(Num(int(input("Enter the value: "))))