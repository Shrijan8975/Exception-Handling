class Student:
    def __init__(self, id = 0 ,nm= "NewStudent"):
        print("I'm constructor...")
        self.rollno =  id
        self.name =  nm

    def __str__(self):
        data = "\nRoll No.: "+str(self.rollno)
        data += "\nName.: "+str(self.name)
        return data

    def __del__(self):
        print("I'm destructor...")

if(__name__ == '__main__'):
    s1= Student(111,"Sumit") 
    print(s1)
