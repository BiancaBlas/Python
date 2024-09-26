primes = list()
print(primes)
"""
primes.append(2)
primes.append(3)
primes.append(5)
primes.append(7)
primes.append(11)
primes.append(13)
""" #this code makes a list and adds numbers at the end

primes = [2, 3, 5, 7, 11]
primes.append(13)
print(primes)

values = [True, False, False, True]

bag = [1, 2, 3]
bag.append("Amber")
bag.append(True)
bag.append(4)
#with most programming languages it is not possible to add different types in one container

print(bag)

list = ["Bart", "Damon", "Loki"]
name = list[2]

def is_valid_index(index: int, list: list) -> bool:
    result = False
    if 0 <= index and index < len(list):
        result = True
    return result

index = 2
print(f"Index {index} is valid" if is_valid_index(index, list) else f"Index {index} is out of range")