# # sum of 1st n off natural number
# def fun_sum_odd(n):
#     if n==1:
#         return 1
#     else:
#         return  (2*n-1)+fun_sum_odd(n-1)
     


# n =int(input("enter the value of n:"))
# print(fun_sum_odd(n))

# #sum of 1st n natural even number
# def sum_even(n):
#     if n==1:
#         return 2
#     else:
#         return (2*n)+sum_even(n-1)


# n= int(input("enter the value of n:"))
# print(sum_even(n))


# #factorial of a number
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
    

# n =int(input("enter the value of n:"))
# print(fact(n))

#sum of squares of 1st n natural number
def sum_squares(n):
    if n==1:
        return 1
    else:
       return (n*n)+sum_squares(n-1)

n =int(input("enter the number:"))
print(sum_squares(n))