student = {
    "name": "Raneya",
    "age": 17,
    "country": "Pakistan",
    "course": "Python"
}

for key in student:
    print(key)

# this prints name, age, country, course

for value in student.values()
    print(value)

# this prints out actual information: raneya, 17, pakistan, Python

# loop through both keys and values

for key, value in student.items():
    print(key, ":", value)

# output: name : raneya, age : 17, country : pakistan, course : Python

