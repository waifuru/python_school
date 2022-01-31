class Animal:

    def __init__(self, age, name):  # конструктор
        self.agea = age
        self.namea = name
        print("я животное")

    def say_hello(self):
        print("Привет я -", self.namea, "и мне", self.agea, "лет")


class Canidaes:

    def __init__(self, age, name):  # конструктор
        self.agea = age
        self.namea = name
        print("я псина")

    def eat(self):
        print("Я покушал!")


class Dog(Canidaes, Animal):

    def __init__(self, color_lejenka, age, name):  # конструктор
        super().__init__(age, name)
        self.color_lejanka = color_lejenka

    def bark(self):
        print("Меня зовут", self.namea, "и у меня", self.color_lejanka, "лежанка")


class Cat(Animal):

    def __init__(self, color_osheinik, age, name):  # конструктор
        super().__init__(age, name)
        self.color_osheinik = color_osheinik

    def meow(self):
        print("Меня зовут", self.namea, "и у меня", self.color_osheinik, "ошейник")


if __name__ == '__main__':


    grisha = Cat("зеленый", 5, "Гриша")


    marsik = Dog("красная", 6, "Марсик")
    marsik.say_hello()
    marsik.bark()
