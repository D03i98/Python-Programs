def animal_cracker(str):
    words = str.split()
    if words[0][0] == words[1][0]:
        return True
    else:
        return False
print(animal_cracker("Hello Python"))