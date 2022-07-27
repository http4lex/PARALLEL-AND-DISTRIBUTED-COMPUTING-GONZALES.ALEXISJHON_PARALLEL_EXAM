import random

prime = []
odd = []
divisible = []
numbers = []
containsNine = []
even = []

for x in range(100):
    num = random.randint(100, 999)

    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

    if num % 9 == 0:
        divisible.append(num)

    dividends = 0
    for y in range(1, num):
        if num % y == 0:
            dividends += 1

    if dividends == 2:
        prime.append(num)

    if "9" in str(num):
        containsNine.append(num)

    numbers.append(num)

print("Printing all numbers...")
for x in numbers:
    print(x)
print("\nPrinting all odd numbers...")
for x in odd:
    print(x)
print("\nPrinting all even numbers...")
for x in even:
    print(x)
print("\nPrinting all numbers divisible by 9...")
for x in divisible:
    print(x)
print("\nPrinting all prime numbers...")
for x in prime:
    print(x)
print("\nPrinting all numbers containing the number 9...")
for x in containsNine:
    print(x)