import random

"""
В клас Human я добавив поле health (здоров'я).
Створив клас Sport
Добавив в клас Human методи:
 - get_sport, який з sport_list вибирає вид спорту
 - sporting, який вибирається випадково в методі live
   і добавляє здоров'я та задоволення залежно від виду спорту,
   крім того перевіряється в методі live рівень здоров'я (неменше 20)
В методах chill та shopping (manage == "delicacies") здров'я зменшується
"""

brands_of_car = {
"BMW":{"fuel":100, "strength":100,"consumption": 6},
"Lada":{"fuel":50, "strength":40,"consumption": 10},
"Volvo":{"fuel":70, "strength":150,"consumption": 8},
"Ferrari":{"fuel":80, "strength":120,"consumption": 14},
}

job_list = {
"Java developer":{"salary":50, "gladness_less": 10 },
"Python developer":{"salary":40, "gladness_less": 3 },
"C++ developer":{"salary":45, "gladness_less": 25 },
"Rust developer":{"salary":70, "gladness_less": 1 },
}

sport_list = {
"Теніс":{"health_plus":50, "gladness_plus": 10 },
"Футбол":{"health_plus":70, "gladness_plus": 15 },
"Карате":{"health_plus":20, "gladness_plus": 8 },
"Плавання":{"health_plus":100, "gladness_plus": 20 },
}

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, sport=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.health = 15
        self.job = job
        self.sport = sport
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_sport(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.sport = Sport(sport_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
        self.satiety += 5
        self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def sporting(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.gladness += self.sport.gladness_plus
        self.health += self.sport.health_plus

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("Заправились")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Купили їжу")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Ура! Нямка!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15
            self.health -= 20

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        self.health -= 10

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Сьогодні {day} з життя {self.name} "
        print(f"{day:=^50}", "\n")
        human_indexes = self.name + " індекси"
        print(f"{human_indexes:^50}", "\n")
        print(f"Гроші – {self.money}")
        print(f"Ситість – {self.satiety}")
        print(f"Здоров'я – {self.health}")
        print(f"Щастя – {self.gladness}")
        home_indexes = "Інформація про будинок"
        print(f"{home_indexes:^50}", "\n")
        print(f"Їжа – {self.home.food}")
        print(f"Безлад – {self.home.mess}")
        car_indexes = f"Стан машини {self.car.brand}"
        print(f"{car_indexes:^50}", "\n")
        print(f"Паливо – {self.car.fuel}")
        print(f"Кількість поїздок до ТО – {self.car.strength}")

    def is_alive(self):
        if self.gladness < 0:
            print("Депресія…")
            return False
        if self.satiety < 0:
            print("Вмер…")
            return False
        if self.money < -500:
            print("Банкрот…")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Вибираємо будинок")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"Вибираємо машину {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"У мене немає роботи, я збираюсь отримати роботу {self.job.job} з зарплатою {self.job.salary}")
        if self.sport is None:
            self.get_sport()
            print(f"Я почав займатися видом спорту: {self.sport.sport}")
        self.days_indexes(day)

        rand = random.randint(1, 5)
        if self.satiety < 20:
            print("Я пішов їсти")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                print("Я хочу відпочити, але занадто брудно")
            else:
                print("Все чудовo, йду чілити")
                self.chill()
        elif self.money < 0:
            print("Треба йти працювати")
            self.work()
        elif self.health < 20:
            print("Треба розтрясти жир і зайнятись спортом")
            self.sporting()
        elif self.car.strength < 15:
            print("Мені треба ремонтувати моє корито")
            self.to_repair()
        elif rand == 1:
            print("Все чудовo, йду чілити")
            self.chill()
        elif rand == 2:
            print("Треба йти працювати")
            self.work()
        elif rand == 3:
            print("Йду поприбираю")
            self.clean_home()
        elif rand == 4:
            print("Час на солодощі")
            self.shopping(manage="delicacies")
        elif rand == 5:
            print("Треба розтрясти жир і зайнятись спортом")
            self.sporting()

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list (brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Машина не може їхати")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

class Sport:
    def __init__(self, sport_list):
        self.sport = random.choice(list(sport_list))
        self.health_plus = sport_list[self.sport]["health_plus"]
        self.gladness_plus = sport_list[self.sport]["gladness_plus"]

h1 = Human("Роман")
for i in range(8):
    if h1.live(i) == False:
        break