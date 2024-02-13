# custom sort order
dog_breeds = ["Golden Retriever", "Labs", "German Shepherd", "Bulldog", "Beagles", "Pitty's", "Boxer"]
sorted_dog_breeds = sorted(dog_breeds, key=lambda breed: (len(breed), breed))

print("Sorted Dog Breeds:", sorted_dog_breeds)

# made beagles plural to so we can see that it will sort alphabetically