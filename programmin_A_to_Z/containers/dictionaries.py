#dictionaries must have unique keys, but can have duplicate values
#dictionaries are unordered
ssn_name_pairs = {} #{} creates an empty dictionary, but you can alo use dict()


ssn_name_pairs = {"666-666-666": "Damon Blasweiler",
                  "123-234-345": "Amber Blasweiler",
                  "123-345-456": "Loki Blasweiler"}
ssn_name_pairs["123-456-789"] = "John Appleseed"
ssn_name_pairs["000-000-002"] = "Dwight Schrute"
ssn_name_pairs["000-000-005"] = "Pam Beesly" 
#order matters, if I put those other 3 names obove the {} part, it gets deleted

#print(ssn_name_pairs)
print(ssn_name_pairs["123-234-345"])

ssn_name_pairs["000-000-002"] = "Mara Blasweiler" #changes the name from Dwight to Mara
ssn_name_pairs["666-222-555"] = "Gizmo Blasweiler" # adds Gizmo to the dictionary

del ssn_name_pairs["123-456-789"]

key = "000-000-005"
if key in ssn_name_pairs:
    del ssn_name_pairs[key]
else:
    print(f"{key} is not in dictionary")

print(ssn_name_pairs)
