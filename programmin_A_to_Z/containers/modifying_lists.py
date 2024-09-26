primes = [2, 3, 5, 7, 11]
print(primes)
primes[1] = 17
print(primes)

primes.append(13)
print(primes)

primes.insert(1, 3)
print(primes)

n = primes.pop(2) #removes items from the list
print(f"Element {n} removed. The primes list became {primes}")

primes.remove(5) #removes a value, not an index
print(primes)
