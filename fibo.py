def recursice_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursice_nth_fibo(n-1) + recursice_nth_fibo(n-2)



def main():
    n = int(input("Počet členů Fibonacciho posloupnosti: "))
    seq = [recursice_nth_fibo(num)] for num in range(n+1)]
    return seq




if __name__ == "__main__":
    main()
