class Student():
    def __init__(self, name, age, group_number, GPA):
        self.name = name
        self.age = age
        self.group_number = group_number
        self.GPA = GPA
        self.money = 0
    def info(self):
        return f"Имя: {self.name}, Age: {self.age}, Group Number: {self.group_number}, GPA: {self.GPA}"
    def fee(self):
        if self.GPA == 5:
            self.money = 6000
            return "Полная стипендия - 6000 Rubles"
        elif self.GPA >= 4:
            self.money = 4000
            return "Частичная стипендия - 4000 Rubles"
        else:
            return "Нет стипендии"
    def fee_comparison(self, other):
        if self.money > other.money:
            return f"{self.name} имеет большую стипендию, чем {other.name}"
        elif self.money < other.money:
            return f"{other.name} имеет большую стипендию, чем {self.name}"
        else:
            return f"{self.name} и {other.name} имеют одну и ту же стипендию"

class Aspirant(Student):
    def __init__(self, name, age, group_number, GPA, research_topic):
        super().__init__(name, age, group_number, GPA)
        self.research_topic = research_topic       
    def fee(self):
        if self.GPA == 5:
            self.money = 8000
            return "Полная стипендия - 8000 Rubles"
        elif self.GPA >= 4:
            self.money = 6000
            return "Частичная стипендия - 6000 Rubles"
        else:
            return "Нет стипендии"
    def info(self):
        return f"Имя: {self.name}, Age: {self.age}, Group Number: {self.group_number}, GPA: {self.GPA}, Research Topic: {self.research_topic}"   
student1 = Student("Иван", 20, "1010", 4.6)
student2 = Aspirant("Олег", 22, "2020", 4, "Machine Learning")
print(f"{student1.info()}\n{student1.fee()}\n{student2.info()}\n{student2.fee()}\n{student1.fee_comparison(student2)}")
