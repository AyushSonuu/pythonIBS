'''"Assign19: 

Implement Below hierarchy

Person - name, age, height

Employee(Person) - emp_id, salary

Manager(Employee) - dept

Implement
- ctor
- display
- get_input

(Deadline 4 Mar)"'''
class person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height

    def display(self):
        print(self.name,self.age,self.height)
    
    def get_input(self):
        self.name=input("Enter name: ")
        self.age=int(input("Enter age: "))
        self.height=int(input("Enter height: "))

    def __str__(self):
        return f"{self.name}, {self.age}, {self.height}"
    
    def __repr__(self):
        return f"{self.name}, {self.age}, {self.height}"
    
class employee(person):

    def __init__(self,name,age,height,emp_id,salary):
        super().__init__(name,age,height)
        self.emp_id=emp_id
        self.salary=salary
    
    def display(self):
        super().display()
        print(self.emp_id,self.salary)

    def get_input(self):
        super().get_input()
        self.emp_id=int(input("Enter emp_id: "))
        self.salary=int(input("Enter salary: "))

    def __str__(self):
        return f"{super().__str__()}, {self.emp_id}, {self.salary}"
    
    def __repr__(self):
        return f"{super().__repr__()}, {self.emp_id}, {self.salary}"
    
class manager(employee):

    def __init__(self,name,age,height,emp_id,salary,dept):
        super().__init__(name,age,height,emp_id,salary)
        self.dept=dept

    def display(self):
        super().display()
        print(self.dept)

    def get_input(self):
        super().get_input()
        self.dept=input("Enter dept: ")

    def __str__(self):
        return f"{super().__str__()}, {self.dept}"
    
    def __repr__(self):
        return f"{super().__repr__()}, {self.dept}"
    




if __name__=="__main__":
    p1=person("Rahul",25,1.80)
    p1.display()
    p1.get_input()
    print(p1)

    e1=employee("Rahul",25,1.80,123456,100000)
    e1.display()
    e1.get_input()
    print(e1)

    m1=manager("Rahul",25,1.80,123456,100000,"HR")
    m1.display()
    m1.get_input()
    print(m1)

    print(m1.dept)