def contagem(n):
       print(n)
       if n== 0:
              return
       else:
              contagem(n-1)

def fatorial(n):
       print(n)
       if n==0 or n==1:
              return 1
       else:
              return n* fat(n-1)

def fibonaci(n):
       a, b = 0, 1
       while a < n:
         print(a, end=' ')
         a, b = b, a+b
       print()


