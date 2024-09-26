part1 = "Stay hungry."
part2 = "Stay foolish."

quote = part1 + " " + part2
print(quote)

quote = f"{part1} {part2}" #formatted string literal
print(quote)

name = "Loki"
age = 7
message = f"Your name is {name} and you are {age} years old."
print(message)

pi = 3.14159265359
message_2 = f"The number pi is approximately equal to {pi:.2f}" # 2 variables
print(message_2)

print(len(message)) #number of characters in message including punctiuation and spaces

uppercase_message = message.upper()
print(uppercase_message)
#same can be done with lower cases
lowercase_message = uppercase_message.lower()
print(lowercase_message)

swappedcase_message = message.swapcase()
print(swappedcase_message)

you_count = message.count("you")
print(f"Count of you in {message} is {you_count}")