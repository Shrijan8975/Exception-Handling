class InvalidAgeErr(Exception):
    def __init__(self, age):
        print("jjjsck")
        self.age =age

    def __str__(self):
        return str(self.age) +" is Invalid age.\nPlease enter the age greater than 18..."
