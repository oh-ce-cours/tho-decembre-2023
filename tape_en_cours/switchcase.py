age = 10

if age > 90:
    print("You are too old to party, granny.")
elif age < 0:
    print("You're yet to be born")
elif age >= 18:
    print("You are allowed to party")
else: 
    print("You're too young to party")

# Output: You are too old to party, granny.

match age:
    case age<0:
        print("too young")