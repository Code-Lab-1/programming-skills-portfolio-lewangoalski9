pets = {
    'animal type': 'tiger',
    'name': 'victor',
    'owner': 'ahmed',
    'weight': 68,
    'eats': 'flesh',
}
pets.append(pets)

pet = {
    'animal type': 'duck',
    'name': 'chickaa',
    'owner': 'arham',
    'weight': 4,
    'eats': 'rice',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'tommy',
    'owner': 'danish',
    'weight': 37,
    'eats': 'cat',
}
pets.append(pet)


for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")