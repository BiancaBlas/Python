primes = [2, 3, 5, 7, 11]

#for number in primes:
#    print (number)
"""
index = 0
while index < len(primes):
    print(primes[index])
    index += 1
"""
#same code as the for in loops

even_numbers = []
odd_numbers = []

for number in primes:
    if number % 2 == 0:
        #print(f"{number} is even")
        even_numbers.append(number)
    else:
        #print(f"{number} is odd")
        odd_numbers.append(number)

print("Even number(s)")
for i in even_numbers:
    print(i)

print("Odd number(s)")
for i in odd_numbers:
    print(i)

ssn_name_pairs = {"666-666-666": "Damon Blasweiler",
                  "123-234-345": "Amber Blasweiler",
                  "123-345-456": "Loki Blasweiler"}

keys = ssn_name_pairs.keys()
values = ssn_name_pairs.values()

print(f"Dictionary keys")
for key in keys:
    print(key)

print(f"Dictionary values")
for value in values:
    print(value)

key_value_pairs = ssn_name_pairs.items()
for key_value in key_value_pairs:
    print(key_value)

for(key, value) in key_value_pairs:
    print(key, value)