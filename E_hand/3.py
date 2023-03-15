z=0
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    try:
        z = x / y
    except ZeroDivisionError:
        print("Nested try: Please enter second value other than zero..")
        raise
    except:
        print("Nested try: Error.....")
except ValueError:
    print("Outer try: Please Enter numeric value only..")
except ZeroDivisionError:
        print("Outer try: Please enter second value other than zero..")
except:
    print("Outer try: Error.....")
else:
    print("Outer try: z:",z)