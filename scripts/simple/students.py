


""" Looping through lists and dicts"""
students = {
        "male": ["Tom", "Charlie", "Harry", "Frank"],
        "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

""" prinit the names witch have the latter a in them """

for key in students.keys(): # first get the key
    print(students[key])
    for name in students[key]:#  then get the value for each key
        """ for every name in that list get the ones including a"""
        if "a" in name:
            print (name)
