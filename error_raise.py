# val = int(input("Enter the value between 5 and 9: "))

# if(val < 5 or val > 9):
#     raise ValueError("Value Should be 5 and 9")
# print(f"Value is {val}")

val = input("Enter the value between 5 and 9, or type 'quit' to exit: ")

if val == "quit":
    print("You chose to quit.")
else:
    val2 = int(val)
    if val2 < 5 or val2 > 9:
        raise ValueError("Value should be between 5 and 9")
    print(f"Value is {val}")
