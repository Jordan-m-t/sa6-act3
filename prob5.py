# Exponential mapping
def raise_to_power(numbers, n):
# using the lambda and map function to raise each number to the power of n
    powered_numbers = list(map(lambda x: x**n, numbers))
    return powered_numbers

numbers_list = [2, 3, 4, 5, 6, 7, 8]
power_of_n = 2

result = raise_to_power(numbers_list, power_of_n)
print(f"Numbers raised to the power of {power_of_n} {numbers_list} equal:", result)
