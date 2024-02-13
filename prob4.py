# Intersection of two lists
def find_intersection(list1, list2):
# using the filter and lambda function to find the intersection
    intersection = list(filter(lambda x: x in list2, list1))
    return intersection

list1 = [1, 2, 3, 4, 5, 9, 4]
list2 = [3, 4, 5, 6, 7, 4, 10, 55, 15, 7]

result = find_intersection(list1, list2)
print("Intersection of the two lists:", result)
