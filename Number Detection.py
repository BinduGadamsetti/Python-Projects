import math

print("=" * 45)
print("        🔍 NUMBER DETECTIVE")
print("=" * 45)

number = int(input("Enter a number: "))

# Positive, Negative or Zero
if number > 0:
    sign = "Positive"
elif number < 0:
    sign = "Negative"
else:
    sign = "Zero"

# Even or Odd
if number % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"


# Prime number check
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


# Perfect square check
def is_perfect_square(n):
    if n < 0:
        return False

    root = math.isqrt(n)
    return root * root == n


# Sum of digits
def digit_sum(n):
    n = abs(n)
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total

# Number_of_digits
def number_of_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


# Palondrome check
def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

# Results
print("\n" + "=" * 45)
print("           🔎 ANALYSIS")
print("=" * 45)

print(f"Number          : {number}")
print(f"Type            : {sign}")
print(f"Even / Odd      : {parity}")
print(f"Prime           : {'Yes' if is_prime(number) else 'No'}")
print(
    f"Perfect Square  : "
    f"{'Yes' if is_perfect_square(number) else 'No'}"
)
print(f"Digit Sum       : {digit_sum(number)}")
print(f"Number of Digits: {number_of_digits(number)}")
print(f"Palindrome      : {'Yes' if is_palindrome(number) else 'No'}")

print("=" * 45)