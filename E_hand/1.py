try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    z = x / y
except ValueError:
    print("Please Enter numeric value only..")
except ZeroDivisionError:
    print("Please enter second value other than zero..")
except:
    print("Error.....")
else:
    print(z)