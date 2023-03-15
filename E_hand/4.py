from InvalidAgeError import InvalidAgeError
try:
    age = int(input("Enter age: "))
    if(age >= 18):
        print("Valid age")
    else:
        raise InvalidAgeError(age)
except ValueError:
    print("Please enter numeric value...")
except InvalidAgeError as e:
    print(e)
