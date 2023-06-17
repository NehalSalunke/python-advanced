class Employee:
    empCount=0
    empNation='India'
    def __init__(self,getname,getsalary=20000):
        self.name=getname
        self.salary=getsalary
        Employee.empCount += 1

    def displayEmployee(self):#Object Method
        print("name:",self.name,"\nSalary: ", self.salary)
        print("Country: ",self.empNation)
    @classmethod #U were not able to call method by class
    def displayCount(self): #class method
        print("total employee :",self.empCount)
        print("Nation: ", self.empNation)
    @staticmethod# u were not able to call method
    def addNumbers(x,y):
        return x+y

if __name__=="__main__":
    e1=Employee('Gaurav',45000)
    e2= Employee('Aditya')
    e2.displayEmployee()
    e2.displayCount()
    print("**********************")
    Employee.displayCount()
    print(e2.addNumbers(89,11))