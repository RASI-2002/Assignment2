class Student:
    def __init__(self,name,mark):
        self.name=name
        self.marks=mark
    def get_grade(self):
        if self.marks >=90:
            return "A"
        elif self.marks >=70:
            return "B"
        else:
            return "C"
students=[Student("D.Kani",98),Student("M.Meha",72),Student("L.Sri",56)]
for stu in students:
    print(f"Name: {stu.name} scored {stu.marks} mark - Grade:{stu.get_grade()}") 
          
