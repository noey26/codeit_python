# 사전 (dictionary)
# key-value pair (키-값 쌍)
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}
print(type(my_dictionary))

print(my_dictionary[3])

my_dictionary[9] = 81
print(my_dictionary)

print(my_dictionary.values())
print(25 in my_dictionary.values())

for value in my_dictionary.values():
    print(value)

for key in my_dictionary.keys():
    value = my_dictionary[key]
    print(key, value)

for key, value in my_dictionary.items():
    print(key, value)

