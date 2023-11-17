pets = {
    'animal type': 'tiger',
    'name': 'victor',
    'owner': 'ahmed',
    'weight': 68,
    'eats': 'flesh',
}
pets.append(pets)

pets = {
    'animal type': 'duck',
    'name': 'chickaa',
    'owner': 'arham',
    'weight': 4,
    'eats': 'rice',
}
pets.append(pets)

pets = {
    'animal type': 'dog',
    'name': 'tommy',
    'owner': 'danish',
    'weight': 37,
    'eats': 'cat',
}
pets.append(pets)


for pets in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")