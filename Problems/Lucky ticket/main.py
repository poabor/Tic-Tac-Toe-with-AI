# Save the input in this variable
ticket = '090234'

# Add up the digits for each half
half1 = sum([int(x) for x in ticket[0:3]])
half2 = sum([int(x) for x in ticket[3:6]])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")