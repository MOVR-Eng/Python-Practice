def fib(a,b,n):
     while a<n:
         print(a,end=' ')
         a,b=b,a+b
     print()
fib(0,1,1000)
