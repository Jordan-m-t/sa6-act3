# sum of digits

sum_of_digits = lambda num: sum(int(digit) for digit in str(num))
number = int(input("Enter a number: "))

result = sum_of_digits(number)

print(f"The sum of digits in your number {number} is: {result}")
