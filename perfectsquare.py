'''
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example:1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
Given an integer n, return the least number of perfect square numbers that sum to n.
'''

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