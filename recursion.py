def tail_recursion(i,n):
    if i > n:
        return
    else:
        print(i)
        tail_recursion(i+1,n)
        
def head_recursion(n, i):
    if i > n:
        return
    else:
        head_recursion(n, i+1)
        print(i)
        
def tail_head_recursion(i, n):
    if i > n:
        return
    else:
        print(i)
        tail_head_recursion(i+1, n)
        print(i)

tail_recursion(1,10)
head_recursion(10,1)
tail_head_recursion(1, 10)
