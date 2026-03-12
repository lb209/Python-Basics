from abc import ABC, abstractmethod

# =========================
# Abstract Class (Abstraction)
# =========================
class Employee(ABC):
    def __init__(self, name):
        # Encapsulation: private variable
        self.__name = name

    # method to access private name
    def display_name(self):
        return self.__name

    # abstract method for salary
    @abstractmethod
    def calculate_salary(self):
        pass

    # abstract method for work (Polymorphism)
    @abstractmethod
    def work(self):
        pass

# =========================
# Child Class 1
# =========================
class Developer(Employee):
    def calculate_salary(self):
        return 50000

    def work(self):
        return "Writes code"

# =========================
# Child Class 2
# =========================
class Manager(Employee):
    def calculate_salary(self):
        return 100000

    def work(self):
        return "Manages team"

# =========================
# Object Creation + Direct Output
# =========================
dev = Developer("Ali")
mgr = Manager("Mr. Khan")

# Developer Output
print("=== Developer Info ===")
print("Name:", dev.display_name())
print("Salary:", dev.calculate_salary())
print("Work:", dev.work())

# Manager Output
print("\n=== Manager Info ===")
print("Name:", mgr.display_name())
print("Salary:", mgr.calculate_salary())
print("Work:", mgr.work())