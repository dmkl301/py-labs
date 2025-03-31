def get_number():
    while True:
        try:
            n = int(input("Enter a number: "))
            return n
        except ValueError:
            print("Please enter a number.")

def sum_numbers(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def prime_num(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


def main():
    n =  get_number()

    print(f"Сума: {sum_numbers(n)}")
    print(f"Факторіал: {factorial(n)}")
    print(f"Ціле число: {prime_num(n)}")

main()