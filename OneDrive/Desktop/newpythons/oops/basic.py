class person :  # object 
     name = "bablu"
     cocuppations = "Softwere Developer"
     networth = 18 

     def info(self):
          print(f"{self.name} is a {self.cocuppations}")
                             # self mean that is who that is calling 
a = person()
b = person()
a.name = "vishal"
b.name = "Aman"
a.cocuppations = "Accountant"
b.cocuppations = "HR"
# print(a.name,a.cocuppations)
a .info()
b.info()
