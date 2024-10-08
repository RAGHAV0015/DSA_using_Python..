def fun(n):
    if n==1:
        return 1
    else:
        return n+fun(n-1)
    



n= float(input("enter the value of n:"))
print(fun(n))

#n natural nubers in reverse order
def fun(n):
    if n==0:
        return 1
    else:
        fun(n-1)
        print(n,end= ' ')

n=int(input("enter the value of n:"))
fun(n)


def fun_reverse(n):
    if n==0:
        return 1
    

#n natural number in reverse order

def funs(n):
    if n==0:
        return 1
    else:
        
        print(n,end= ' ')
        funs(n-1)

n=int(input("enter the value of n:"))
funs(n)

#print 1st odd n natural numbers

def fun_odd(n):
    if n==0:
        return 1
    else:
        fun_odd(n-1)
        print(2*n-1,end=' ')
n =int(input("enter the value of n:"))
fun_odd(n)

#print first n even number
def fun_even(n):
    if n==1:
        return 2
    else:
        
        fun_even(n-1)
        print(2*n,end='  ')

n =int(input("enter the n:"))
fun_even(n)
#print 1st n odd natural number in reverse order
def fun(n):
    if n==1:
        return 1
    else:
        print(2*n-1,end=' ')
        fun(n-1)
n=int(input("enter the value of n:"))
fun(n)
