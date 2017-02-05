
def oddOccurrencesInArray(array):
    search = 0

    for num in array:
        search ^= num # XOR operators

    return search


array = [ 3, 5, 3, 5, 6, 8, 6, 8, 7 ]
print (oddOccurrencesInArray(array))
