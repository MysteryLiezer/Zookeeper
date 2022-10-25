# Save the input in this variable ticket = ...
# Add up the digits for each half

ticket = input()

ticket_list = [int(x) for x in str(ticket)]

half1 = sum(ticket_list[:3])
half2 = sum(ticket_list[3:])

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")