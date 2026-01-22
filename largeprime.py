def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(num ** 0.5) + 1
    for d in range(3, limit, 2):
        if num % d == 0:
            return False
    return True
def largest_prime_with_digits(d: int) -> int | None:
    if d <= 0:
        return None
    low = 10 ** (d - 1)
    high = 10 ** d - 1
    if high % 2 == 0:
        high -= 1
    for num in range(high, low - 1, -2):
        if is_prime(num):
            return num
    return None
if __name__ == "__main__":
    d = int(input("Enter the number of digits: "))
    result = largest_prime_with_digits(d)
    if result is None:
        print("No prime exists with that number of digits.")
    else:
        print(f"The largest prime with {d} digits is {result}.")