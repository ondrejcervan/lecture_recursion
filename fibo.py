# def recursice_nth_fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return recursice_nth_fibo(n-1) + recursice_nth_fibo(n-2)


def recursive_binary_search(arr, target, left, right):
    if right >= left:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return recursive_binary_search(arr, target, left, mid - 1)
        else:
            return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return None

def main():
    # n = int(input("Počet členů Fibonacciho posloupnosti: "))
    # seq = [recursice_nth_fibo(num)] for num in range(n+1)]
    # return seq
    import json
    with open('sequential.json', 'r') as file:
        data = json.load(file)
    arr = data['array']
    target = data['target']
    result = recursive_binary_search(arr, target, 0, len(arr) - 1)

    if result is not None:
        print(f"Hledaná hodnota {target} byla nalezena na indexu {result}.")
    else:
        print(f"Hledaná hodnota {target} se v seznamu nenachází.")



if __name__ == "__main__":
    main()
