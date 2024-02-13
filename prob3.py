# Finding Maximum
def find_maximum(numbers, compare_function):
    if not numbers:
        return None
# Initializing the maximum with the first element of the list
    maximum = numbers[0]
# iterating over the list.
    for num in numbers[1:]:
        maximum = compare_function(maximum, num)
    return maximum

numbers_list = [30, 15, 25, 75, 45, 35, 55, 15]
greater_of_two = lambda x, y: x if x > y else y

result = find_maximum(numbers_list, greater_of_two)
print("Maximum Number:", result)
