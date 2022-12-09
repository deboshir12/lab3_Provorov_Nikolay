class Employee():
    
    def __init__(self, salary, premium_ratio,count_hours):
        self.salary = salary
        self.premium_ratio = premium_ratio
        self.count_hours = count_hours
    def info(self):
        print(f'Колличество рабочих часов: {self.count_hours}')
        print(f'Зарплата : {self.salary} руб.')
        print(f'Коэффициень премии: {self.premium_ratio}')
    def salary_to_hours(self):
        print(f'Соотношение зарплаты к рабочим часам: {self.salary/self.count_hours}')
        
        
class Senior_employee(Employee):
    def __init__(self, salary, premium_ratio, count_hours):
        super().__init__(salary, premium_ratio,count_hours)
    def calculate_premium(self):
        print(f'Премия: {self.premium_ratio * self.salary}')    
        
class Director(Senior_employee):
    def __init__(self, salary, premium_ratio,count_hours):
        super().__init__(salary, premium_ratio, count_hours)
    '''def salary_to_hours(self):
        print(f'Соотношение зарплаты к рабочим часам: {self.salary/self.count_hours}')'''
    '''def info(self):
        super().info()'''
    
f = Employee(50000, 1.3,1200)
f.info()
s = Senior_employee(50000, 1.3,1200)
s.calculate_premium()
s.salary_to_hours()
print("\n")
a = Director(80000, 1.5, 1200)
a.info()
a.calculate_premium()
a.salary_to_hours()