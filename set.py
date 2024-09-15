# ahmed = set()
# print(type(ahmed))


def check(n):
    return (n & 1) == 1

val = check(5000)
if val:
    print("The value is Odd")
else:
    print("The value is Even")
