def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return[0, 1]
    else:
        seq_fib = fibonacci(n - 1)
        seq_fib.append(seq_fib[-1] + seq_fib[-2])
        return seq_fib
    
num = float(input("digite um numero"))
res = fibonacci(num)

print(f"sequencia de fibonacci::  {res}")
    


    


      
