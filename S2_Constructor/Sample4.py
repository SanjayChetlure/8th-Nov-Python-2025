class Demo4:

    def __init__(self,empName,empId,empSalary,empDesignation):
        self.empName=empName          #assign local variable info into class variable
        self.empId=empId
        self.empSalary=empSalary
        self.empDesignation=empDesignation

    def empInfo(self):
        print("Employee Name:-",self.empName)
        print("Employee ID:-", self.empId)
        print("Employee Salary:-", self.empSalary)
        print("Employee Designation:-", self.empDesignation)


emp1=Demo4("Amol",101,50000.3,"Automation Tester")
emp2=Demo4("Rahul",102,40000.5,"Manual Tester")
emp3=Demo4("Junaid",103,20000.5,"Manual Tester")

emp1.empInfo()
print("--")
emp2.empInfo()
print("--")
emp3.empInfo()


