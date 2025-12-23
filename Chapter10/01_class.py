class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000


akshara = Employee()
akshara.name = "Akshara" # This is an instance attribute
print(akshara.name,akshara.language, akshara.salary)

rohan = Employee()
rohan.name = "Rohan  Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is instance attribute and salary and language are class attributes as they directly belong to the class