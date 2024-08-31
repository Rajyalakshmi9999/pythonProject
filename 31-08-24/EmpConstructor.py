
# Constructor
# Special Function in Class,  __init__()
# It will be automatically called when you create an Object

class Employee:
    name = None
    eid = None
    phone = None
    age = None
    city = None

    def __init__(self,name,eid,phone,age,city):
        print("Called, Object is created")
        self.name = name
        self.age = age
        self.eid = eid
        self.phone = phone
        self.city = city



    def display(self):
        print("data display")
        print("This is the Employee data -> ", self.name, self.age,self.eid,self.phone,self.city)
        return None


emp11 = Employee(input("name :"),int(input("age:")) ,input("email:"),int(input("phone:")),input("city:"))
print(emp11.name)
print(emp11.age)
print(emp11.eid)
print(emp11.city)
print(emp11.phone)

emp11.display()  # ->

