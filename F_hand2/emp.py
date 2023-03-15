class Emp:
    def __init__(self, id = 0 , nm="newEmp", sal = 25000):
        self.eid = id
        self.ename = nm
        self.salary = sal
    
    def __str__(self):
        data = "Emp Id: "+str(self.eid)
        data += "\nEmp Name: "+str(self.ename)
        data += "\nEmp Salary: "+str(self.salary)
        return data
