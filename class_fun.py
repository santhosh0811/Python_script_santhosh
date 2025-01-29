class person:
    
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
        


    def details_person(self):
        print(f"The name of the person is {self.name},age is {age},and height is {height}")
    

    def details1_person(self):
        print("init")

name=input("enter thr name of the person:\n")
age=int(input("enter the age of the person:\n"))
height=float(input("enter the heght of the person:\n"))        

P1=person(name,age,height)
#P2=person("san")

P1.details_person()
P1.details1_person()

