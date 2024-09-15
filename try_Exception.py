val = int(input("Enter the number: "))
while(val > 0):
    try:
        val = int(input("Enter the number: "))
        if(val < 0):
            raise ValueError("Value should not be less than 0")
        for i in range(1 ,11):
            print(f"{val} X {i} = {val * i}")
    except Exception as e:
        print(f"{e}")

    finally:
        print("Executed Successfully")

