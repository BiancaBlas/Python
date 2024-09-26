balance = 5000
money = 5000
if balance >= money:
    balance -= money
    print(f"Current balance is {balance}")
    print("Transaction complete. Don't forget your card.")
else:
    print("Insufficient funds")
    print(f"Current balance is {balance}")

#you can use if statements without else statements

number = 12
if number % 2 == 0:  # modulo, devides and gives the remainder after division
    print("The number is even")
if number > 10:
    print("The number is greater than ten")
if number == 12:
    print("A dozen")

traffic_light = "red"
if traffic_light == "green":
    print("Go!")
#elif traffic_light == "yellow":
 #   print("Slow down and prepare to stop")
elif traffic_light == "red":
    if traffic_light == "blinking":
        print("Stop! Proceed when safe.")
    else:
        print("Stop!")

else:
    print("Invalid state.")



#avoid too deeply nested code. max 2 times nested. You can use and operators
# if traffic_light == "red" and is_blinking

succes = True
result_code = 200

if succes == True and result_code == 200:
    print("Succes")
else:
    print("Failure")

first_name = "Ellen"
last_name = "Ripley"

if len(first_name) == 0 or len(last_name) == 0:
    print("Please enter your name")
else: print(f"Hi {first_name} {last_name}")

admin_user = False

if not admin_user:
    print("Permission denied!")


