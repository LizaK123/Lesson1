from datetime import date

class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age

class Driver(Person):
    def __init__(self, name, birth_date, license_number):
        super().init(name, birth_date)
        self.license_number = license_number

    def display_driver_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.get_age()} років")
        print(f"Номер водійського посвідчення: {self.license_number}")


person = Person("Олександр", date(1990, 5, 20))
print(f"{person.name} має {person.get_age()} років")

driver = Driver("Іван", date(1985, 10, 15), "AB1234567")
driver.display_driver_info()
